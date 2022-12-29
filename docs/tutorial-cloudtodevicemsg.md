---
title: Light up an LED 
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Send a Message to a Simulated Device

In this tutorial you'll create a simulated device message listener, send a message to your device from the cloud, then verify the message appears in your listener.  Following the diagram below:

1. Create and run a simulated device listener in a command prompt.  Your listener will use its Device Connection string from the IoT Hub `Device Management > Devices` to connect your application directly to your IoT hub.
1. Send a message from the cloud to your simulated device. Your cloud application will use the IoT Hub Connection string and the device identifier to send the message.
1. Verify the message was received by your simulated device listener.

![lnk_sendmessage]
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
- Completed the tutorial to [Create a Symmetric Key Device](tutorial-symmetrickeydevice.md)

## Create a message listener for your device

See the [Azure IoT device library](https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device?view=azure-python)

1. Open Visual Studio Code, select File > Open Folder... and select your `various` GitHub cloned directory.
1. From your Visual Studio Code terminal session, change the GitHub cloned directory from `various` to `python` directory.
1. Create a file in the `python` directory and name it `c2dlistener.py`.  This file is the python code in your device that listens for messages from your instance IoT Hub.
1. Copy and paste the following import statements into your `c2dlistener.py` file.

    ```python
    import time
    from azure.iot.device import Message, IoTHubDeviceClient
    ```

    Table of code details
    |Import  |Comment  |
    |---------|---------|
    |`time` |  Used for the code execution to sleep while awaiting for incoming messages |
    |`Message` | The `Message` class from the `azure.iot.device` is needed to read and print the size and data of the message. Install the library by opening a python terminal session and running the script `pip install azure-iot-device` |
    |`IoTHubDeviceClient` | The `IoTHubDeviceClient` from the `azure.iot.device` is needed to communicate to your IoT Hub. |

1. Copy and paste below the following function to receive incoming messages from IoT Hub. Note this function prints the size of the message and payload upon receiving the message in IoT Hub.

    ```python
    def message_handler(message):
        print("--Message Received--")
        print("size={size}kb".format(size=(Message(message).get_size()/1000)))
        print("payload={data}".format(data=Message(message).data))
    ```

1. Copy and paste the main function below the message handler function. Replace `IOTHUB_DEVICE_CONNECTION_STRING` with your device connection string. See the [blog on different connection strings](https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/) to obtain your device connection string. This function creates the client, registers the message handler to receive incoming messages, and gracefully shuts down the client.

    ```python
    def main():
        conn_str = "IOTHUB_DEVICE_CONNECTION_STRING"
        client = IoTHubDeviceClient.create_from_connection_string(conn_str)
        print("--Simulated Device Waiting for Messages--") 
        print("  (Type ctrl-c to exit this application)")
        
        try:
            client.on_message_received = message_handler
            while True:
                #ctrl-c to exit
                time.sleep(1000)
        except KeyboardInterrupt:
            print("Messaging device sample stopped")
        finally:
            # Graceful exit
            print("Shutting down IoT Hub Client")
            client.shutdown()
    
    if __name__ == "__main__":
        main()
    ```

    Table of code details
    |IoT Hub Client Call  |Comment  |
    |---------|---------|
    | client = IoTHubDeviceClient.create_from_connection_string(conn_str) | Creates a client from the IoT Hub device connection string. The client is used to make calls to IoT Hub. |
    | client.on_message_received = message_handler | Registers the message event handler for IoT Hub to call to the client. |
    | client.shutdown() | Gracefully disconnects the client from IoT Hub. |

1. Open a PowerShell session and change to the `python` directory in your GitHub cloned `various` repo.

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

    If your listener doesn't start due to an error, then troubleshoot it by [running the debugger](https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger) in Visual Studio Code.

## Send message

1. Create a file in the `python` directory and name it `c2dsendmsg.py`.  This file is the python code to send a message to your device via your IoT Hub instance.
1. Copy and paste the import statement.

    ```python
    from azure.iot.hub import IoTHubRegistryManager
    ```

1. Copy and past the following code.

    ```python
    registry_manager = IoTHubRegistryManager("IOTHUB_CONNECTION_STRING")
    
    try:
        registry_manager.send_c2d_message(input("Device id: "), input("Message to send: "), {})
    except Exception as ex:
            print ( "Unexpected error {0}" % ex )
    ```

1. From Visual Studio Code, create a .env file in the root of your GitHub clone directory `variable`. Visual Studio Code terminal session, add your `IOTHUB_CONNECTION_STRING` environment variable to the `.env` file. See the [blog on different connection strings](https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/) to obtain your IoT Hub connection string.

    ```powershell
    IOTHUB_CONNECTION_STRING="{your IoT hub connection string}"
    ```

    For example,
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

<!--images-->

[lnk_sendmessage]: media/tutorial-cloudtodevicemsg/simulatedmessage.png
