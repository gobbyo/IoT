from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager
import os

def main():
    deviceId = input("Device id: ")
    props={}

    try:
        registry_manager = IoTHubRegistryManager(os.getenv('IOTHUB_CONNECTION_STRING'))
        # assign system properties
        props.update(messageId = "{0}".format(uuid4()))
        props.update(contentEncoding = "utf-8")
        props.update(contentType = "application/json")

        payload = '{ "state":"on","order":["0","1","2","3","4","5","6","7","8","9"],"pause":".25" }'
        #payload = '{ "state":"off","order":["5","7","1","3","0","4","2","9","8","6"],"pause":".25" }'

        registry_manager.send_c2d_message(deviceId, payload, props)
    except Exception as ex:
        print ( "Unexpected error {0}".format(ex) )

if __name__ == "__main__":
    main()