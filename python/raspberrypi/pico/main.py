from machine import Pin, RTC, UART
import network, rp2, time
import urequests
import json
import time
import secrets

def syncclock(rtc):
    print("Sync clock")
    try:
        externalIPaddress = urequests.get('https://api.ipify.org').text
    except:
        externalIPaddress = "45.115.204.194"
    finally:
        print("Obtaining external IP Address: {0}".format(externalIPaddress))
    
    timeAPI = "https://www.timeapi.io/api/Time/current/ip?ipAddress={0}".format(externalIPaddress)
    print(timeAPI)
    r = urequests.get(timeAPI)
    universal = json.loads(r.content)
    timeAPI = "https://www.timeapi.io/api/TimeZone/zone?timeZone={0}".format(universal["timeZone"])
    print(timeAPI)
    r = urequests.get(timeAPI)
    j = json.loads(r.content)
    t = (j["currentLocalTime"].split('T'))[1].split(':')
    rtc.datetime((int(universal["year"]), int(universal["month"]), int(universal["day"]), 0, int(t[0]), int(t[1]), int(universal["seconds"]), 0))

def main():
    rtc = RTC()
    # set your WiFi Country
    rp2.country('US')

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # set power mode to get WiFi power-saving off (if needed)
    wlan.config(pm = 0xa11140)

    wlan.connect(secrets.ssid, secrets.pwd)

    while not wlan.isconnected() and wlan.status() >= 0:
        print("connecting...")
        time.sleep(1)

    syncclock(rtc)
    uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
    uart.init(9600, bits=8, parity=None, stop=1)
    print("UART is configured as : ", uart)

    while True:
        s = "{:0>2d}".format(rtc.datetime()[5])
        print(s)
        uart.write(json.dumps(s))
        time.sleep(60)

if __name__ == "__main__":
    main()