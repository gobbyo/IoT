import RPi.GPIO as GPIO
import time
import asyncio
import json
from decouple import config
from azure.iot.device import Message, X509
from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient

#   7 segmented LED
#
#        _a_
#     f |_g_| b
#     e |___| c _h
#         d
# num   hgfe dcba   hex
#
# 0 = 	0011 1111   0x3F
# 1 =	0000 0110   0x06
# 2 =	0101 1011   0x5B
# 3 =	0100 1111   0x4F
# 4 =	0110 0110   0x66
# 5 =	0110 1101   0x6D
# 6 =	0111 1101   0x7D
# 7 =	0000 0111   0x07
# 8 =   0111 1111   0x7F
# 9 =   0110 0111   0x67

pins = [19,21,8,10,12,29,31,16]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
provisioning_host = config("DPS_HOST")
id_scope = config("DPS_SCOPEID")
registration_id = config("DPS_REGISTRATIONID")

def message_handler(message):
    print("--Message Received--")
    try:
        payload = json.loads(message.data)
        repeat = int(payload['repeat'])
        repeatpause = int(payload['repeatpause'])
        seq = list(payload['time'])
        if payload('pm') == "True":
            pm = True
        pause = float(payload['pause'])
        for i in range(repeat):
            for s in seq:
                num = segnum[int(s)]
                if pm:
                    num |= 0x01 << 7
                paintnumbers(num)
                time.sleep(pause)
            paintnumbers(0) #clear the last digit
            time.sleep(repeatpause)
    finally:
        print("--Message Processed--")

def paintnumbers(val):
    i = 0
    for pin in pins:
        GPIO.output(pin,(val & (0x01 << i)) >> i)
        i += 1

async def main():
    print("Ctrl-c to quit'")
    GPIO.setmode(GPIO.BOARD)

    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

    print("Creating x509 cert object from file. Code id = 3a931dc7-9028-409f-be9f-7065fe6de8eb")
    x509 = X509(
        cert_file=config("X509_CERT_FILE"),
        key_file=config("X509_KEY_FILE"),
        pass_phrase=config("X509_PASS_PHRASE"),
    )

    print("Creating provisioning client from certificate. Code id = 53503ead-4f5a-4b8c-b129-9d95120db1b5")
    provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
        provisioning_host=provisioning_host,
        registration_id=registration_id,
        id_scope=id_scope,
        x509=x509,
    )

    print("Registering provisioning client. Code id = 334527c8-5958-4915-b5f6-e24753d275c4")
    registration_result = await provisioning_device_client.register()

    if registration_result.status == "assigned":
        device_client = IoTHubDeviceClient.create_from_x509_certificate(
            x509=x509,
            hostname=registration_result.registration_state.assigned_hub,
            device_id=registration_result.registration_state.device_id,
        )

    print("Connecting client to IoT hub. Code id = dace1ead-91dd-4f3e-bbc9-a74d6b08bc1a")
    await device_client.connect()

    device_client.on_message_received = message_handler

    try:
        print("--Waiting for message--")
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        await device_client.shutdown()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    asyncio.run(main())