from machine import Pin, RTC
import scrolltext
import network, rp2, time
import urequests
import json
import secrets

def syncclock(rtc):
    print("Sync clock")
    print("Obtaining external IP Address")
    externalIPaddress = "45.115.204.194" #default
    try:
        externalIPaddress = urequests.get('https://api.ipify.org').text
        print("Obtained external IP Address: {0}".format(externalIPaddress))
    except:
        print("Unable to obtain external IP Address, using default: {0}".format(externalIPaddress))
    
    timeAPI = "https://www.timeapi.io/api/Time/current/ip?ipAddress={0}".format(externalIPaddress)
    r = urequests.get(timeAPI)
    z = json.loads(r.content)
    timeAPI = "https://www.timeapi.io/api/TimeZone/zone?timeZone={0}".format(z["timeZone"])
    print(timeAPI)
    rq = urequests.get(timeAPI)
    j = json.loads(rq.content)
    t = (j["currentLocalTime"].split('T'))[1].split(':')
    #[year, month, day, weekday, hours, minutes, seconds, subseconds]
    rtc.datetime((int(z["year"]), int(z["month"]), int(z["day"]), 0, int(t[0]), int(t[1]), int(z["seconds"]), 0))

def main():
    rowpins = [26,18,9,20,2,8,3,6]
    colpins = [19,4,5,22,7,21,17,16]

    stext = scrolltext.scrolldisplay()
    stext.rowpins = rowpins
    stext.colpins = colpins

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

    rtc = RTC()
    syncclock(rtc)

    while True:
        #[year, month, day, weekday, hours, minutes, seconds, subseconds]
        t = rtc.datetime()
        buf = "Today is {1}/{2}/{0}".format(t[1], t[2], t[0])
        print(buf)
        stext.scroll(buf,2)
        buf = "{:002d}:{:002d}".format(t[3], t[4])
        print(buf)
        stext.scroll(buf,2)

        r = urequests.get("https://api.open-meteo.com/v1/forecast?latitude=48.50&longitude=-122.71&current_weather=true&hourly=relativehumidity_2m,pressure_msl")
        j = json.loads(r.content)
        buf = 'Temp {0} f'.format(32+(9/5*float(j['current_weather']['temperature'])))
        print(buf)
        stext.scroll(buf,2)

        buf = 'Wind {0} mph @ {1} degrees'.format(j['current_weather']['windspeed'], j['current_weather']['winddirection'])
        print(buf)
        stext.scroll(buf,2)

        pressure = j['hourly']['pressure_msl']
        humitity = j['hourly']['relativehumidity_2m']

        buf = 'Pressure {0}'.format(pressure[len(pressure)-1])
        print(buf)
        stext.scroll(buf,2)
        buf = 'Humidity {0}'.format(humitity[len(humitity)-1])
        print(buf)
        stext.scroll(buf,2)

if __name__ == "__main__":
    main()