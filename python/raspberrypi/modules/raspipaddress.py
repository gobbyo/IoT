import socket
import os

def get_ip_address():
    ip_address = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("1.1.1.1",80))
        ip_address = s.getsockname()[0]
        s.close()
    except socket.error as e:
        print("Error: {0}. CodeID = 7c931613-a37c-4631-9f30-ccfc3ed028f1".format(e))
    return ip_address

def get_host_name():
    return socket.gethostname()

def get_public_address():
    return os.system('curl api.ipify.org')
