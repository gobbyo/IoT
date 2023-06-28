import network
import socket
import secrets
import time

from machine import Pin
import uasyncio as asyncio

led = Pin(15, Pin.OUT)
onboard = Pin("LED", Pin.OUT, value=0)

html = """<!DOCTYPE html>
<html>
    <head> <title>clock server test</title> </head>
    <body> <h1>Set up network for clock</h1>
        <p>%s</p>
    </body>
</html>
"""

wlan = network.WLAN(network.STA_IF)

def connect_to_network():
    wlan.active(True)
    wlan.config(pm = 0xa11140)  # Disable power-save mode
    wlan.connect(secrets.ssid,secrets.pwd)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            #STAT_IDLE – no connection and no activity,
            #STAT_CONNECTING – connecting in progress,
            #STAT_WRONG_PASSWORD – failed due to incorrect password,
            #STAT_NO_AP_FOUND – failed because no access point replied,
            #STAT_CONNECT_FAIL – failed due to other problems,
            #STAT_GOT_IP – connection successful
            print('wlan.status() = {0}'.format(wlan.status()))
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        conf = wlan.ifconfig()
        print(conf)

async def serve_client(reader, writer):
    print("Client connected")
    request_line = await reader.readline()
    print("Request:", request_line)
        
    response = html
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)

    await writer.drain()
    await writer.wait_closed()
    print("Client disconnected")

async def main():
    print('Connecting to Network...')
    connect_to_network()
    print('Setting up webserver...')
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 80))
    while wlan.isconnected():
        print("Online")
        await asyncio.sleep(5)
    
    print("Offline")
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()