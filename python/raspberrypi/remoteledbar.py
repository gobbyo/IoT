import RPi.GPIO as GPIO
import asyncio
import time
import json
from decouple import config
from azure.iot.device import Message, X509
from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient

LED_pins = [8,12,16,18,22,24,26,32,36,38]
provisioning_host = config("DPS_HOST")
id_scope = config("DPS_SCOPEID")
registration_id = config("DPS_REGISTRATIONID")

def message_handler(message):
    print("--Message Received--")
    try:
        payload = json.loads(message.data)
        seq = list(payload['order'])
        pause = float(payload['pause'])

        for s in seq:
            print("pin:{0}, state:{1}".format(LED_pins[int(s)], payload['state']))

            if payload['state'] == 'on':
                GPIO.output(LED_pins[int(s)], GPIO.HIGH)
            else:
                GPIO.output(LED_pins[int(s)], GPIO.LOW)   
            time.sleep(pause)

    finally:
        print("--Message Processed--")

async def main():
    print("Ctrl-c to quit'")
    GPIO.setmode(GPIO.BOARD)

    for p in LED_pins:
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