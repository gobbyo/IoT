import socket
from decouple import config
from azure.iot.device import IoTHubDeviceClient, exceptions

def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

def main():
    try:
        hostname = socket.gethostname()
        ip_address = get_ip_address()

        msg = '{{ "Hostname:{0}", "IPAddress:{1}" }}'.format(hostname, ip_address)
        print("Hostname: {0}".format(hostname))
        print("IP address: {0}".format(ip_address))
        client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))
        client.send_message(msg)
    finally:
        print("complete")

if __name__ == "__main__":
    main()