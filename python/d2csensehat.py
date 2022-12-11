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

    msg = Message(json.dumps('{{ "msgsent_utc":"{0}", "fahrenheit":"{1}", "humdity":"{2}", "pressure":"{3}" }}'.format(datetime.utcnow().isoformat(),t,h,b)))
    msg.content_type = 'application/json;charset=utf-8'
    client.send_message(msg)

def main():
    try:
        sense = SenseHat()
        client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))

        while True:
            get_stats(sense, client)
            time.sleep(60.0)

    except KeyboardInterrupt:
        print("Device sample stopped")
    finally:
        # Graceful exit
        print("Clearing sensor")
        sense.clear()

if __name__ == "__main__":
    main()