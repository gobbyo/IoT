import time
from datetime import datetime
from decouple import config
from azure.iot.device import IoTHubDeviceClient
from azure.iot.device import exceptions
from sense_hat import SenseHat

def main():
    background = (0,0,0)
    color = (150,150,150)

    try:
        sense = SenseHat()

        f = (sense.temperature * 9/5) + 32
        t = "temp: %3.0f"%f
        print(t)
        sense.show_message(t,0.05,color,background)

        u = "humidity: %3.0f"%sense.humidity
        print(u)
        sense.show_message(u,0.05,color,background)

        p = "pressure: %2.0f"%sense.pressure
        print(p)
        sense.show_message(p,0.05,color,background)

        s = time.strftime('%I:%M %p')
        print(s)
        sense.show_message(s,0.05,color,background)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Device sample stopped")
    finally:
        # Graceful exit
        print("Clearing sensor")
        sense.clear()

if __name__ == "__main__":
    main()