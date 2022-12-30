from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager
import os

registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))

try:
    props={}
    # optional: assign system properties
    props.update(messageId = "{0}".format(uuid4()))
    props.update(contentType = "application/json")

    # optional: assign application properties
    props.update(LED = input("On or Off: "))

    registry_manager.send_c2d_message(input("Device id: "), "Update LED", props)
except Exception as ex:
    print ( "Unexpected error {0}" % ex )