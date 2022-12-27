import socket
import modules.raspipaddress as raspipaddress
from datetime import datetime
import time
from decouple import config
from azure.iot.device import IoTHubDeviceClient, exceptions

def main():
    print("[{0}] Send IoT Hub this device's Host Name and IP address. CodeID = b5faac72-eee4-43fe-9af1-33b489c51add".format(datetime.utcnow().isoformat()))
    #wait 30 seconds for the system to get up and running after reboot
    time.sleep(30)
    try:
        hostname = socket.gethostname()
        ip_address = raspipaddress.get_ip_address()

        msg = '{{ "Hostname":"{0}", "IPAddress":"{1}" }}'.format(hostname, ip_address)
        client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))
        client.send_message(msg)
    except exceptions.ClientError as e:
        print("Error: {0}. CodeID = 2f85db08-398e-4997-ab67-b9105a328e0e".format(e))
    finally:
        print("[{0}] Connection string: {1}. CodeID = 2b700d52-b1d2-41ad-8a78-90d59c9d083a".format(datetime.utcnow().isoformat(),config("IOTHUB_DEVICE_CONNECTION_STRING")))
        print("[{0}] Message sent: {1}".format(datetime.utcnow().isoformat(), msg))

if __name__ == "__main__":
    main()