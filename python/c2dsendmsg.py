from uuid import uuid4
from azure.iot.hub import IoTHubRegistryManager, Message

registry_manager = IoTHubRegistryManager("HostName=HubMsgHubw2lu5yeop2qwy.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=92/VHr+94MgD5hOKqvDaUVy/1DGMAQ4aa2l+F7q7mW4=")

try:
    msg = Message()
    msg.message_id = uuid4()
    msg.correlation_id = "correlation-1234"
    msg.custom_properties["LED"] = input("On or Off? ")
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    registry_manager.send_c2d_message(input("Device id: "), msg, {})
except Exception as ex:
    print ( "Unexpected error {0}" % ex )