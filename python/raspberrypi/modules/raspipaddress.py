import socket

def get_ip_address():
    ip_address = ''
    try:
        host = socket.gethostname()
        ip_address = socket.gethostbyname(host)
    except socket.error as e:
        print("Error: {0}. CodeID = 2e798e2d-0802-4b1d-9860-a83e3e35b599".format(e))
    return ip_address