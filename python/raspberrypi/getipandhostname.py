import socket
import time
from decouple import config
from azure.iot.device import IoTHubDeviceClient

def get_ip_address():
    ip_address = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        ip_address = s.getsockname()[0]
        s.close()
    except socket.error as msg:
        print("Error: {0}".format(msg))
    return ip_address

def main():
    #wait 30 seconds for the system to get up and running after reboot
    time.sleep(30)
    try:
        hostname = socket.gethostname()
        ip_address = get_ip_address()

        msg = '{{ "Hostname":"{0}", "IPAddress":"{1}" }}'.format(hostname, ip_address)
        print(msg)
        client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))
        client.send_message(msg)
    finally:
        print("Completed getipandhostname.py")

if __name__ == "__main__":
    main()