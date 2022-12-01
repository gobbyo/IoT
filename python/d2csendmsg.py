from azure.iot.device import IoTHubDeviceClient

device_client = IoTHubDeviceClient.create_from_connection_string(input("IoT Hub Device connection string:"))
device_client.connect()
device_client.send_message(input("Message:"))
device_client.shutdown()