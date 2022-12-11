import time
import json
from datetime import datetime
from decouple import config
from azure.iot.device import IoTHubDeviceClient, Message
from sense_hat import SenseHat

def get_stats(sense, client):
    background = (0,0,0)
    color = (145, 141, 10)
    s = time.strftime('%I:%M %p')
    print(s)
    sense.show_message(s,0.05,color,background)

    sense.clear()

    f = (sense.temperature * 9/5) + 32
    t = "temp: %f3.0"%f
    print(t)
    sense.show_message(t,0.05,color,background)

    u = "humidity: %3.0f"%sense.humidity
    print(u)
    sense.show_message(u,0.05,color,background)

    p = "pressure: %2.0f"%sense.pressure
    print(p)
    sense.show_message(p,0.05,color,background)

    msg = '{{ "sent_utc":"%s", "fahrenheit":"%3.0f", "humidity":"%3.0f", "pressure":"%2.0f" }}'%(datetime.utcnow().isoformat(),sense.temperature,sense.humidity,sense.pressure)
    client.send_message(msg)

def main():
    try:
        sense = SenseHat()
        client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))

        while True:
            get_stats(sense, client)
            time.sleep(300.0)

    except KeyboardInterrupt:
        print("Device sample stopped")
    finally:
        # Graceful exit
        print("Clearing sensor")
        sense.clear()

if __name__ == "__main__":
    main()