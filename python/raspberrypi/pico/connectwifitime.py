from machine import Pin, RTC
import network, rp2, time
import urequests
import json
import time
import secrets

def main():
    # set your WiFi Country
    rp2.country('US')

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # set power mode to get WiFi power-saving off (if needed)
    wlan.config(pm = 0xa11140)

    wlan.connect(secrets.usr, secrets.pwd)

    while not wlan.isconnected() and wlan.status() >= 0:
        print("connecting...")
        time.sleep(1)

    print("externl IP = {0}".format(urequests.get('https://api.ipify.org').text))
    r = urequests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles")
    j = json.loads(r.content)

    print("{0}, {1} {2}".format(j["dayOfWeek"],j["date"],j["time"]))

    time.sleep(1)

if __name__ == "__main__":
    main()