from decouple import config
from azure.iot.hub import IoTHubRegistryManager

registry_manager = IoTHubRegistryManager(config("IOTHUB_CONNECTION_STRING"))

try:
    registry_manager.send_c2d_message(input("Device id: "), input("Message to send: "), {})
except Exception as ex:
        print ( "Unexpected error {0}" % ex )