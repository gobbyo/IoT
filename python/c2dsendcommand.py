import os
import json
from azure.iot.hub import IoTHubRegistryManager

registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))

deviceId = input("Device id: ")
msg = input("Message: ")
print(msg)

props={}

try:
    registry_manager.send_c2d_message(deviceId, msg, props)
except Exception as ex:
        print ( "Unexpected error {0}" % ex )