import os
import time
from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager

data = '{ "pause": "0.25", "pm": "True", "time": [0,2,2,3] }'

def main():
    deviceId = "raspberrypi2"

    try:
        registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))
        
        # assign system properties
        props={}
        props.update(messageId = "{0}".format(uuid4()))
        props.update(contentType = "application/json")

        registry_manager.send_c2d_message(deviceId, data, props)
    except Exception as ex:
        print ( "Unexpected error {0}" % ex )

if __name__ == "__main__":
    main()