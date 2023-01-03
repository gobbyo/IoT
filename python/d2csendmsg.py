import os
from azure.iot.device import IoTHubDeviceClient, Message

client = IoTHubDeviceClient.create_from_connection_string(os.getenv("IOTHUB_DEVICE_CONNECTION_STRING"))
msg = Message('{ "sample_message":"Hello World!" }')
msg.content_type = 'application/json;charset=utf-8'

client.send_message(msg)