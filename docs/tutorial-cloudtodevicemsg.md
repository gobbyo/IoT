# Send a message to your device

In this tutorial you'll send a message to your device from the cloud.

[todo] image needed

## Prerequisites

[todo]

## Create a message listener for your device

See the [Azure IoT device library](https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device?view=azure-python)

1. Open Visual Studio Code, select File > Open Folder... and select your `various` GitHub cloned directory.
1. From your Visual Studio Code terminal session, change the GitHub cloned directory from `various` to `python` directory.
1. Create a file in the `python` directory and name it `c2dlistener.py`.  This file is the python code on your device that listens for messages from your instance IoT Hub.
1. Copy and paste the following import statements into your `c2dlistener.py` file.

    ```python
    import asyncio
    import time
    from azure.iot.device.aio import IoTHubDeviceClient
    ```

    Table of code details
    |Import  |Comment  |
    |---------|---------|
    |`asyncio` | Needed to asyncronously `await` for messages from your IoT Hub instance |
    |`time` |  Used for the code execution to sleep while awaiting for incoming messages |
    |`IoTHubDeviceClient` | The `IoTHubDeviceClient` from the `azure.iot.device.aio` is needed to communicate to your IoT Hub |

1. Copy and paste below the import statements the following function to receive incoming messages from IoT Hub. Note this function prints the entire incoming message.

    ```python
    def message_handler(message):
        print("--Message Received--")
        print(message)
    ```

1. Copy and paste the main function below the message handler function. This function creates the client, registers the message handler to receive incoming messages, and gracefully shuts down the client.  It is important to call the shutdown function on the client to gracefully disconnect it from IoT Hub.

    ```python
    async def main():
        conn_str = input("Device Connection String:")
        client = IoTHubDeviceClient.create_from_connection_string(conn_str)
        print("--Waiting for Messages--") 
        
        try:
            client.on_message_received = message_handler
            while True:
                #ctrl-c to exit
                await time.sleep(1000)
        except KeyboardInterrupt:
            print("Messaging device sample stopped")
        finally:
            # Graceful exit
            print("Shutting down IoT Hub Client")
            await client.shutdown()
    
    if __name__ == "__main__":
        asyncio.run(main())
    ```

    Table of code details
    |IoT Hub Client Call  |Comment  |
    |---------|---------|
    | client = IoTHubDeviceClient.create_from_connection_string(conn_str) | Creates a client from the IoT Hub device connection string. The client is used to make calls to IoT Hub. |
    | client.on_message_received = message_handler | Registers the message event handler for IoT Hub to call to the client. |
    | client.shutdown() | Gracefully disconnect the client from IoT Hub. |

1. Open a command prompt and change to the `python` directory in your GitHub cloned `various` repo.
1. [todo] How to get the device connection string
1. Run the following script to start the listener.

    ```python
    python c2dlistener.py
    ```

    For example,

    ```python
    C:\repos\various\python>python c2dlistener.py
    IoT Hub *Device* Connection String:HostName=HubMsgHubw2lu5yeop2qwy.azure-devices.net;DeviceId=myDevice;SharedAccessKey=8IrOf5TrNmo17wv7upTAHllOVVIaL4tkq65E3YtZUkg=
    --Waiting for Messages--
    ```

## Send a message to your device

1. Create a file in the `python` directory and name it `c2dsendmsg.py`.  This file is the python code to send a message to your device via your IoT Hub instance.
1. Copy and paste the import statement.

    ```python
    from azure.iot.hub import IoTHubRegistryManager
    ```

1. Copy and past the following code.

    ```python
    deviceId = input("Device id: ")
    registry_manager = IoTHubRegistryManager(input("IoT Hub Connection String: "))
    registry_manager.send_c2d_message(deviceId, input("Message to send: "), properties={})
    ```

1. Get your deviceId.
1. Get the connection string to IoT Hub.
1. Run debug in Visual Studio Code.

    ```powershell
    Device id: myDevice
    IoT Hub Connection String: HostName=[IOT HUB NAME].azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=[SHARED ACCESS KEY]
    Message to send: Hello World!
    ```

    Note the following should appear in you `command prompt - python` running `c2dlistener.py`,

    ```powershell
    --Message Received--
    b'Hello World!'
    ```

## Reference

IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages).