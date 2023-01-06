import os
import time
from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager

turnOn = '{ "pause": "0.25", "state": "on", "order": [0,1,2,3,4,5,6,7,8,9] }'
turnOff = '{ "pause": "0.25", "state": "off", "order": [0,1,2,3,4,5,6,7,8,9] }'

def main():
    deviceId = "raspberrypi2"

    try:
        registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))
        
        # assign system properties
        props={}
        props.update(messageId = "{0}".format(uuid4()))
        props.update(contentType = "application/json")

        registry_manager.send_c2d_message(deviceId, turnOn, props)
        time.sleep(2.5)
        registry_manager.send_c2d_message(deviceId, turnOff, props)
    except Exception as ex:
        print ( "Unexpected error {0}" % ex )

if __name__ == "__main__":
    main()