import os
import time
import json
from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager

def main():
    deviceId = "raspberrypi2"

    try:
        registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))
        
        # assign system properties
        props={}
        props.update(messageId = "{0}".format(uuid4()))
        props.update(contentType = "application/json")

        j = {}
        j.update(repeat = 5)
        j.update(repeatpause = 1)
        j.update(pause = 0.5)
        t = []
        hour = time.gmtime().tm_hour
        
        if hour > 12:
            j.update(pm = 'True')
            hour -= 12
        else:
            j.update(pm = 'False')

        h = str(hour).zfill(2)
        m = str(time.gmtime().tm_min).zfill(2)
        t.append(int(h[0]))
        t.append(int(h[1]))        
        t.append(int(m[0]))
        t.append(int(m[1]))
        j.update(time = t)
        data = json.dumps(j)
        registry_manager.send_c2d_message(deviceId, data, props)
    except Exception as ex:
        print ( "Unexpected error {0}" % ex )

if __name__ == "__main__":
    main()