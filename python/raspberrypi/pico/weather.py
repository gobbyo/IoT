import scrolltext
from machine import Pin
import network, rp2, time
import urequests
import json
#import ntptime

def main():
    day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    rowpins = [26,18,9,20,2,8,3,6]
    colpins = [19,4,5,22,7,21,17,16]

    stext = scrolltext.scrolldisplay()
    stext.rowpins = rowpins
    stext.colpins = colpins

    # set the time
    #ntptime.settime()
    #UTC_OFFSET = -8 * 60 * 60

    # set your WiFi Country
    rp2.country('US')

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # set power mode to get WiFi power-saving off (if needed)
    wlan.config(pm = 0xa11140)

    wlan.connect('Clipper', 'Orcatini')

    while not wlan.isconnected() and wlan.status() >= 0:
        print("connecting...")
        time.sleep(1)

    while True:
        #t = time.localtime(time.time() + UTC_OFFSET)
        #buf = "Today is {0}, {1}. {2}, {3}".format(day[t[6]], month[t[1]-1], t[2], t[0])
        #stext.scrolltext(buf,2)
        #buf = "{:002d}:{:002d}".format(t[3], t[4])
        #stext.scrolltext(buf,2)

        r = urequests.get("https://api.open-meteo.com/v1/forecast?latitude=48.50&longitude=-122.71&current_weather=true&hourly=relativehumidity_2m,pressure_msl")
        j = json.loads(r.content)
        buf = 'Temp {0} f'.format(32+(9/5*float(j['current_weather']['temperature'])))
        stext.scrolltext(buf,2)

        buf = 'Wind {0} mph @ {1} degrees'.format(j['current_weather']['windspeed'], j['current_weather']['winddirection'])
        stext.scrolltext(buf,2)

        pressure = j['hourly']['pressure_msl']
        humitity = j['hourly']['relativehumidity_2m']

        buf = 'Pressure {0}'.format(pressure[len(pressure)-1])
        stext.scrolltext(buf,2)
        buf = 'Humidity {0}'.format(humitity[len(humitity)-1])
        stext.scrolltext(buf,2)

if __name__ == "__main__":
    main()