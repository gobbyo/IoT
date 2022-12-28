import asyncio
import socket
import uuid
from decouple import config
from azure.iot.device import Message,X509
from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient
import modules.raspipaddress as raspipaddress

provisioning_host = config("DPS_HOST")
id_scope = config("DPS_SCOPEID")
registration_id = config("DPS_REGISTRATIONID")

async def send_message(device_client):
    print("sending message")
    hostname = socket.gethostname()
    ip_address = raspipaddress.get_ip_address()
    
    msg = Message('{{ "Hostname":"{0}", "IPAddress":"{1}" }}'.format(hostname, ip_address) )
    msg.message_id = uuid.uuid4()
    await device_client.send_message(msg)
    print("message sent: {0} ".format(msg))

async def main():
    x509 = X509(
        cert_file=config("X509_CERT_FILE"),
        key_file=config("X509_KEY_FILE"),
        pass_phrase=config("X509_PASS_PHRASE"),
    )

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

        # Connect the client.
        await device_client.connect()

        # send `messages_to_send` messages in parallel
        await send_message(device_client)

        # finally, disconnect
        await device_client.disconnect()
    else:
        print("Error: Can not send telemetry from the provisioned device. CodeID = f586eb27-5b36-46fa-ae25-5ffb3ad19efc")


if __name__ == "__main__":
    asyncio.run(main())
