import socket
from decouple import config
from azure.iot.device import IoTHubDeviceClient, exceptions

def get_ip_address():
    print("enter get_ip_address()")
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    print("returning ip_address()")
    return ip_address

def main():
    try:
        hostname = socket.gethostname()
        ip_address = get_ip_address()

        msg = '{{ "Hostname:{0}", "IPAddress:{1}" }}'.format(hostname, ip_address)
        print(msg)
        client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))
        client.send_message(msg)
    except exceptions as e:
        print(e)
    finally:
        print("Completed getipandhostname.py")

if __name__ == "__main__":
    main()