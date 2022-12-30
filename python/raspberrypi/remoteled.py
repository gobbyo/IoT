import RPi.GPIO as GPIO
import asyncio
import time
from decouple import config
from azure.iot.device import Message, X509
from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient

LED_channel = 17

provisioning_host = config("DPS_HOST")
id_scope = config("DPS_SCOPEID")
registration_id = config("DPS_REGISTRATIONID")

def message_handler(message):
    print("--Message Received--")
    try:
        s = message.custom_properties['LED']
        if s == 'On':
            GPIO.output(LED_channel, GPIO.HIGH)
            print("On")
        else:
            GPIO.output(LED_channel, GPIO.LOW)
            print("Off")
    finally:
        print("--Message Processed--")

async def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_channel, GPIO.OUT)
    GPIO.output(LED_channel, GPIO.LOW)

    print("Ctrl-C to quit")

    print("Creating x509 object. Code id = 93f0b0da-2420-42ce-880f-2c14313275c8")
    x509 = X509(
        cert_file=config("X509_CERT_FILE"),
        key_file=config("X509_KEY_FILE"),
        pass_phrase=config("X509_PASS_PHRASE"),
    )

    print("Creating client from certificate. Code id = 93f0b0da-2420-42ce-880f-2c14313275c8")
    provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
        provisioning_host=provisioning_host,
        registration_id=registration_id,
        id_scope=id_scope,
        x509=x509,
    )

    print("Registering client with provisioning service. Code id = e6ce0f4a-665b-42c9-9724-53a9e5d5c174")
    registration_result = await provisioning_device_client.register()

    print(registration_result.registration_state)

    if registration_result.status == "assigned":
        device_client = IoTHubDeviceClient.create_from_x509_certificate(
            x509=x509,
            hostname=registration_result.registration_state.assigned_hub,
            device_id=registration_result.registration_state.device_id,
        )

    # Connect the client.
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