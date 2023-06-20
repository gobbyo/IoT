from machine import Pin, RTC
import network, rp2, time
import urequests
import json
import time
import secrets
import segmentdisplays

def start(segdisp):
    segmentdisplays.showbacknumber(segdisp)
    segmentdisplays.showbackfloat(segdisp)
    segmentdisplays.showforwardfloat(segdisp)
    segmentdisplays.showforwardnumber(segdisp)

def wificonnect():
    rp2.country('US')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # set power mode to get WiFi power-saving off (if needed)
    wlan.config(pm = 0xa11140)

    wlan.connect(secrets.usr, secrets.pwd)

    while not wlan.isconnected() and wlan.status() >= 0:
        print("connecting...")
        time.sleep(1)

def syncclock(rtc):
    print("Sync clock")
    externalIPaddress = urequests.get('https://api.ipify.org').text
    r = urequests.get("https://www.timeapi.io/api/Time/current/ip?ipAddress={0}".format(externalIPaddress))
    j = json.loads(r.content)
    rtc.datetime((int(j["year"]), int(j["month"]), int(j["day"]), 0, int(j["hour"]), int(j["minute"]), int(j["seconds"]), 0))

def main(): 
    rtc = machine.RTC()
    segdisp = segmentdisplays.segdisplays()
    start(segdisp)

    wificonnect()
    syncclock(rtc)
    
    while True:
        segdisp.printclockfloat(rtc.datetime()[5],rtc.datetime()[6])
        segdisp.printnumber(rtc.datetime()[4])

if __name__ == "__main__":
    main()