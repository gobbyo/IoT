from azure.iot.hub import IoTHubRegistryManager

deviceId = input("Device id: ")
registry_manager = IoTHubRegistryManager(input("IoT Hub Connection String: "))
registry_manager.send_c2d_message(deviceId, input("Message to send: "), properties={})