import socket
import modules.raspipaddress as raspipaddress
from datetime import datetime
import time
from decouple import config
from decouple import config
from azure.iot.device import Message, X509, exceptions
from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient

provisioning_host = config("DPS_HOST")
id_scope = config("DPS_SCOPEID")
registration_id = config("DPS_REGISTRATIONID")

async def main():
    print("[{0}] Send IoT Hub this device's Host Name and IP address. CodeID = b5faac72-eee4-43fe-9af1-33b489c51add".format(datetime.utcnow().isoformat()))
    #wait 30 seconds for the system to get up and running after reboot
    time.sleep(30)
    try:
        x509 = X509(
            cert_file=config("X509_CERT_FILE"),
            key_file=config("X509_KEY_FILE"),
            pass_phrase=config("X509_PASS_PHRASE"),
        )
        print("Creating provisioning client. Code Id = f1973054-24af-4a6b-9a79-409abcd7d27f")
        provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
            provisioning_host=provisioning_host,
            registration_id=registration_id,
            id_scope=id_scope,
            x509=x509,
        )
        registration_result = await provisioning_device_client.register()

        if registration_result.status == "assigned":
            device_client = IoTHubDeviceClient.create_from_x509_certificate(
                x509=x509,
                hostname=registration_result.registration_state.assigned_hub,
                device_id=registration_result.registration_state.device_id,
            )

        hostname = socket.gethostname()
        ip_address = raspipaddress.get_ip_address()

        msg = '{{ "Hostname":"{0}", "IPAddress":"{1}" }}'.format(hostname, ip_address)
        await device_client.connect()
        await device_client.send_message(msg)
        await device_client.disconnect()
    except exceptions.ClientError as e:
        print("Error: {0}. CodeID = 2f85db08-398e-4997-ab67-b9105a328e0e".format(e))
    finally:
        print("[{0}] Connection string: {1}. CodeID = 2b700d52-b1d2-41ad-8a78-90d59c9d083a".format(datetime.utcnow().isoformat(),config("IOTHUB_DEVICE_CONNECTION_STRING")))
        print("[{0}] Message sent: {1}".format(datetime.utcnow().isoformat(), msg))

if __name__ == "__main__":
    asyncio.run(main())