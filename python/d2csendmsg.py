import os
from azure.iot.device import IoTHubDeviceClient, Message

client = IoTHubDeviceClient.create_from_connection_string(os.getenv("IOTHUB_DEVICE_CONNECTION_STRING"))
msg = Message('{ "pause": "0.25", "state": "on", "order": [0,1,2,3,4,5,6,7,8,9] }')
msg.content_type = 'application/json;charset=utf-8'

client.send_message(msg)