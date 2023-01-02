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
            print("pin = {0}".format(LED_pins[int(s)]))
            if payload['state'] == 'on':
                GPIO.output(LED_pins[int(s)], GPIO.HIGH)
            else:
                GPIO.output(LED_pins[int(s)], GPIO.LOW)
            time.sleep(pause)

    finally:
        print("--Message Processed--")

async def main():
    GPIO.setmode(GPIO.BOARD)

    for p in LED_pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

    print("Ctrl-C to quit'")
    print("Creating x509 cert object from file. Code id = e28c4236-60bb-4d45-adad-2a1b5cd0302e")
    x509 = X509(
        cert_file=config("X509_CERT_FILE"),
        key_file=config("X509_KEY_FILE"),
        pass_phrase=config("X509_PASS_PHRASE"),
    )

    print("Creating provisioning client from certificate. Code id = 7dc43b15-f17b-4f17-9446-8d26b1e188d2")
    provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
        provisioning_host=provisioning_host,
        registration_id=registration_id,
        id_scope=id_scope,
        x509=x509,
    )

    print("Registering provisioning client. Code id = 4d906cc4-61a9-4fe2-ab6e-4e397f63a702")
    registration_result = await provisioning_device_client.register()

    if registration_result.status == "assigned":
        device_client = IoTHubDeviceClient.create_from_x509_certificate(
            x509=x509,
            hostname=registration_result.registration_state.assigned_hub,
            device_id=registration_result.registration_state.device_id,
        )

    print("Connecting client to IoT hub. Code id = 6893e706-291e-44f5-8623-fea84046866a")
    await device_client.connect()

    device_client.on_message_received = message_handler

    try:
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