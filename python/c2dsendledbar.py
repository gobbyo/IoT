from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager
import time
import os

def main():
    deviceId = input("Device id: ")
    props={}

    try:
        registry_manager = IoTHubRegistryManager(os.getenv('IOTHUB_CONNECTION_STRING'))

        props.update(contentEncoding = "utf-8")
        props.update(contentType = "application/json")

        props.update(messageId = "{0}".format(uuid4()))
        payload = '{ "state":"on","order":["0","1","2","3","4","5","6","7","8","9"],"pause":".25" }'
        registry_manager.send_c2d_message(deviceId, payload, props)
        
        time.sleep(2.5)

        props.update(messageId = "{0}".format(uuid4()))
        payload = '{ "state":"off","order":["0","1","2","3","4","5","6","7","8","9"],"pause":".25" }'
        registry_manager.send_c2d_message(deviceId, payload, props)

    except Exception as ex:
        print ( "Unexpected error {0}".format(ex) )

if __name__ == "__main__":
    main()