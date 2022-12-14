import time
from datetime import datetime
from decouple import config
from azure.iot.device import IoTHubDeviceClient, Message
from sense_hat import SenseHat

def show_stats(sense,color,background):
    sense.clear()

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

def send_stats(sense, client):
    f = (sense.temperature * 9/5) + 32
    msg = '{ "sent_utc":"%sZ", "fahrenheit":"%3.0f", "humidity":"%3.0f", "pressure":"%3.0f" }'%(datetime.utcnow().isoformat(),f,sense.humidity,sense.pressure)
    #print("msg: %s"%msg)
    client.send_message(msg)

def main():
    background = (0,0,0)
    color = (150,150,150)
    i = 0

    try:
        sense = SenseHat()
        client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))

        while True:
            if i >= 3:
                send_stats(sense, client)
                i = 0
            else:
                show_stats(sense,color,background)

            i += 1      
            time.sleep(30.0)

    except KeyboardInterrupt:
        print("Device sample stopped")
    finally:
        # Graceful exit
        print("Clearing sensor")
        sense.clear()

if __name__ == "__main__":
    main()