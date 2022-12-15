import os
import time
import json
import asyncio
from sense_hat import SenseHat

def get_stats(sense):
    background = (0,0,0)
    color = (145, 141, 10)
    s = time.strftime('%I:%M %p')
    print(s)
    sense.show_message(s,0.05,color,background)

    sense.clear()

    c = round(sense.temperature)
    f = round(c * 9/5) + 32
    t = "temp: {0}".format(str(f))
    print(t)
    sense.show_message(t,0.05,color,background)

    u = round(sense.humidity)
    h = "humdity: {0}".format(str(u))
    print(h)
    sense.show_message(h,0.05,color,background)

    o = round(sense.pressure)
    b = "bar: {0}".format(str(o))
    print(b)
    sense.show_message(b,0.05,color,background)

def main():
    try:
        sense = SenseHat()

        while True:
            get_stats(sense)
            time.sleep(10)

    except KeyboardInterrupt:
        print("Device sample stopped")
    finally:
        # Graceful exit
        print("Clearing sensor")
        sense.clear()

if __name__ == "__main__":
    main()