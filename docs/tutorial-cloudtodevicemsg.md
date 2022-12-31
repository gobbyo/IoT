---
title: Send a Message from the Cloud to a Simulated Device
description: Create a simulated device message listener, send a message to your device from the cloud, then verify the message appears in your listener. 
author: jbeman@hotmail.com
---

# Tutorial: Send a Message from the Cloud to a Simulated Device

In this tutorial, you learn how to:

- Create a Message Listener for your Simulated Device
- Send a Message to your Simulated Device from the Cloud

Remotely controlling your device from anywhere in the world is a major feature of using the Internet of Things services. In this tutorial you'll create a simulated device message listener, send a message to your device from the cloud, then verify the message appears in your listener.  Following the diagram below:

1. Create and run a simulated device listener in a command prompt.  Your listener uses its Device Connection string from the IoT Hub to connect your application directly to your IoT hub.
1. Send a message from the cloud to your simulated device. Your cloud application uses the IoT Hub Connection string and the device identifier to send the message.
1. Verify the message was received by your simulated device listener.

![lnk_sendmessage]

## Prerequisites

- Completed the [Tutorial: Create a Simulated Device](tutorial-symmetrickeydevice.md)

## Create a Message Listener for your Simulated Device

This section takes you through the steps to create a listener for your simulated device. The code will be slightly different when we use an actual device, because we'll using the Device Provisioning Service with an x509 certificate rather than use the IoT Hub Connection string.

1. Open Visual Studio Code, select **File > Open Folder...** and select your `various` GitHub forked cloned directory.
1. From your Visual Studio Code terminal session, change the GitHub forked cloned directory from `various` to `python` directory, for example `cd c:\repos\various\python`.
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
    |`IoTHubDeviceClient` | The `IoTHubDeviceClient` from the `azure.iot.device` is needed to communicate to your IoT Hub. For additional information see the [Azure IoT device library](https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device?view=azure-python)|

1. Copy and paste below the following function to receive incoming messages from IoT Hub. Note this function prints the size of the message and payload upon receiving the message in IoT Hub.

    ```python
    def message_handler(message):
        print("--Message Received--")
        print("size={size}kb".format(size=(Message(message).get_size()/1000)))
        print("payload={data}".format(data=Message(message).data))
    ```

1. Copy and paste the main function below the message handler function. Replace `IOTHUB_DEVICE_CONNECTION_STRING` with your device connection string. See the previous tutorial, [Create a Simulated Device](tutorial-symmetrickeydevice.md), to obtain your device connection string. This main function creates the client, registers the message handler to receive incoming messages, and gracefully shuts down the client.

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
    |Key IoT Hub Client Calls  |Comment  |
    |---------|---------|
    | client = IoTHubDeviceClient.create_from_connection_string(conn_str) | Creates a client from the IoT Hub device connection string. The client is used to make calls to IoT Hub. |
    | client.on_message_received = message_handler | Registers the message event handler for IoT Hub to call to the client. |
    | client.shutdown() | Gracefully disconnects the client from IoT Hub. |

1. Open a PowerShell session and change to the `python` directory in your GitHub forked clone `various` repo.

1. Run the following script to start the listener.

    ```python
    python c2dlistener.py
    ```

    For example,

    ```python
    C:\repos\various\python>python c2dlistener.py
    IoT Hub *Device* Connection String:HostName=[IOT HUB NAME].azure-devices.net;DeviceId=myDevice;SharedAccessKey=[SHARED ACCESS KEY]
    --Waiting for Messages--
    ```

    If your listener doesn't start due to an error, then troubleshoot it by [running the debugger](https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger) in Visual Studio Code.

## Send a Message to your Simulated Device from the Cloud

In this section we'll build a simple application that sends a message to your simulated device through IoT Hub. This code pattern is used to send commands from an application, like from a phone, directly to your device.

1. Create a file in the `python` directory and name it `c2dsendmsg.py`.  This file is the python code to send a message to your device via your IoT Hub instance.
1. Copy and paste the import statement.

    ```python
    from azure.iot.hub import IoTHubRegistryManager
    ```

1. Copy and past the following code, then replace `IOTHUB_CONNECTION_STRING` with the actual 

    ```python
    registry_manager = IoTHubRegistryManager("IOTHUB_CONNECTION_STRING")
    
    try:
        registry_manager.send_c2d_message(input("Device id: "), input("Message to send: "), {})
    except Exception as ex:
            print ( "Unexpected error {0}" % ex )
    ```

1. Replace the `IOTHUB_CONNECTION_STRING` by opening the Azure Portal and following the diagram below. 1️⃣ In the left pane, select your IoT Hub service portal page, then 2️⃣ select **Security Settings > Shared access policies**. 3️⃣ In the center pane, select **iothubowner** in the Manage shared access policies section. 4️⃣ Copy the **Primary Connection String** and replace the `IOTHUB_CONNECTION_STRING` in your code you pasted from the previous step.

![lnk_iothubconnection]

1. Open a command prompt, change to your `{github forked clone}/python` directory, then run the following script:

    ```python
    python c2dsendmsg.py
    ```

    For example,

    ```powershell
    c:\repos\various\python> python c2dsendmsg.py
    Device id: myDevice
    Message to send: Hello World!
    ```

1. Verify your messsage listener receives your message in the command prompt running `c2dlistener.py`, for example,

    ```powershell
    --Message Received--
    b'Hello World!'
    ```

## Reference

IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)

## Next Steps

[Tutorial: Send a Message from a Simulated Device To the Cloud](tutorial-devicetocloudmsg.md)

<!--images-->

[lnk_sendmessage]: media/tutorial-cloudtodevicemsg/simulatedmessage.png
[lnk_iothubconnection]: media/tutorial-cloudtodevicemsg/iothubconnection.png
