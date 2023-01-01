from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager
import os

def main():
    deviceId = input("Device id: ")
    s = input("On or Off: ")
    # Add any json to the payload as the content type is set to json
    payload = '{ "remote call": "Update LED" }'
    props={}

    try:
        registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))
        
        # assign system properties
        props.update(messageId = "{0}".format(uuid4()))
        props.update(contentType = "application/json")
        # assign 
        props.update(LEDBar=True)
        payload = '{ "iter":"1", "order":"0,1,2,3,4,5,6,7,8,9", "barpause":".125", "repeatpause":"0.5" }'

        registry_manager.send_c2d_message(deviceId, payload, props)
    except Exception as ex:
        print ( "Unexpected error {0}" % ex )

if __name__ == "__main__":
    main()