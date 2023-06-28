

def web_page(insert):
    html = """<html><head><meta name="picow access point" content="width=device-width, initial-scale=1"></head>
    <body><h1>PicoW</h1><h2>Connection successful from your device {0}</h2></body></html>""".format(insert)
    return html

def main():
    import usocket as socket        #importing socket
    import socket
    import network            #importing network
    import gc
    gc.collect()
    ssid = 'clock'                  #Set access point name 
    password = '12oclock'      #Set your access point password

    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)            #activating

    while ap.active() == False:
        pass
    print('Wifi is ready')
    print(ap.ifconfig())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
    s.bind(('', 80))
    s.listen(5)
    
    #while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    response = web_page(str(addr[0]))
    conn.send(response)
    b = conn.recv(2048)
    print(b.decode('utf-8'))
    conn.close()

if __name__ == '__main__':
    main()