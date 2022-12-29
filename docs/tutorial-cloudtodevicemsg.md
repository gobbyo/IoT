---
title: Light up an LED 
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

<!--
Remove all the comments in this template before you sign-off or merge to the 
main branch.
-->

<!--
This template provides the basic structure of a tutorial article.
See the [tutorial guidance](contribute-how-to-mvc-tutorial.md) in the contributor guide.

To provide feedback on this template contact 
[the templates workgroup](mailto:templateswg@microsoft.com).
-->

<!-- 1. H1 
Required. Start with "Tutorial: ". Make the first word following "Tutorial: " a 
verb.
-->

# Tutorial: Light up an LED 

<!-- 2. Introductory paragraph 
Required. Lead with a light intro that describes, in customer-friendly language, 
what the customer will learn, or do, or accomplish. Answer the fundamental “why 
would I want to do this?” question. Keep it short.
-->

In this tutorial you'll create a message listener, send a message to the cloud, and verify the message appears in your listener.

<!-- 3. Tutorial outline 
Required. Use the format provided in the list below.
-->

In this tutorial, you learn how to:

> [!div class="checklist"]
> * All tutorials include a list summarizing the steps to completion
> * Each of these bullet points align to a key H2
> * Use these green checkboxes in a tutorial

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- Completed the tutorial to [Configure your Windows Machine](tutorial-configure.md)
- Completed the tutorial to [Connect and configure your Raspberry Pi with Visual Studio Code](tutorial-rasp-connect.md)

## Create a message listener for your device

See the [Azure IoT device library](https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device?view=azure-python)

1. Open Visual Studio Code, select File > Open Folder... and select your `various` GitHub cloned directory.
1. From your Visual Studio Code terminal session, change the GitHub cloned directory from `various` to `python` directory.
1. Create a file in the `python` directory and name it `c2dlistener.py`.  This file is the python code on your device that listens for messages from your instance IoT Hub.
1. Copy and paste the following import statements into your `c2dlistener.py` file.

    ```python
    import asyncio
    import time
    from decouple import config
    from azure.iot.device import Message
    from azure.iot.device.aio import IoTHubDeviceClient
    ```

    Table of code details
    |Import  |Comment  |
    |---------|---------|
    |`asyncio` | Needed to asynchronously `await` for messages from your IoT Hub instance |
    |`time` |  Used for the code execution to sleep while awaiting for incoming messages |
    |`os` | Used to get the environment variable containing the connection string to IoT Hub |
    |`Message` | The `Message` class from the `azure.iot.device` is needed to read and print the size and data of the message |
    |`IoTHubDeviceClient` | The `IoTHubDeviceClient` from the `azure.iot.device.aio` is needed to communicate to your IoT Hub |

1. Copy and paste below the import statements the following function to receive incoming messages from IoT Hub. Note this function prints only the size of the message and payload.

    ```python
    def message_handler(message):
        print("--Message Received--")
        print("size={size}kb".format(size=(Message(message).get_size()/1000)))
        print("payload={data}".format(data=Message(message).data))
    ```

1. Copy and paste the main function below the message handler function. This function creates the client, registers the message handler to receive incoming messages, and gracefully shuts down the client.  It is important to call the shutdown function on the client to gracefully disconnect it from IoT Hub.

    ```python
    async def main():
        conn_str = config("IOTHUB_DEVICE_CONNECTION_STRING")
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
    | client.shutdown() | Gracefully disconnects the client from IoT Hub. |

1. Open a PowerShell session and change to the `python` directory in your GitHub cloned `various` repo.
1. Run the following script to register your device connection string replacing `{your device connection string}`. See the [blog on different connection strings](https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/) to obtain your device connection string.

    ```powershell
    IOTHUB_DEVICE_CONNECTION_STRING="{your device connection string}"
    ```

1. Run the following script to start the listener.

    ```python
    python c2dlistener.py
    ```

    For example,

    ```python
    C:\repos\various\python>python c2dlistener.py
    IoT Hub *Device* Connection String:HostName=HubMs*************p2qwy.azure-devices.net;DeviceId=myDevice;SharedAccessKey=8Ir*************tZUkg=
    --Waiting for Messages--
    ```

## Send message

1. Create a file in the `python` directory and name it `c2dsendmsg.py`.  This file is the python code to send a message to your device via your IoT Hub instance.
1. Copy and paste the import statement.

    ```python
    from decouple import config
    from azure.iot.hub import IoTHubRegistryManager
    ```

1. Copy and past the following code.

    ```python
    registry_manager = IoTHubRegistryManager(config("IOTHUB_CONNECTION_STRING"))
    
    try:
        registry_manager.send_c2d_message(input("Device id: "), input("Message to send: "), {})
    except Exception as ex:
            print ( "Unexpected error {0}" % ex )
    ```

1. From Visual Studio Code terminal session, set your `IOTHUB_CONNECTION_STRING` environment variable. See the [blog on different connection strings](https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/) to obtain your IoT Hub connection string.

    ```powershell
    IOTHUB_CONNECTION_STRING="{your IoT hub connection string}"
    ```

1. Run the debugger in Visual Studio Code and provide your deviceId you created from the tutorial [Create a Symmetric Key Device](tutorial-symmetrickeydevice.md). For example,

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

IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)
