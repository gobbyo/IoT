---
title: Send a Message from a Simulated Device To the Cloud
description: [todo] 
author: jbeman@hotmail.com
---

# Tutorial: Send a Message from a Simulated Device To the Cloud

In this tutorial, you learn how to:

- Create device code that sends a message to the Cloud
- Send a Message to your Simulated Device from the Cloud

In this tutorial you'll send messages from your device to the cloud.  There are several reasons why you would have a device send messages to the cloud:

- **Data storage**. The cloud can provide a centralized location to store data collected by IoT devices. This data can then be used for a variety of purposes, such as analytics, machine learning, and more.
- **Remote access**. By sending data to the cloud, IoT devices can allow users to access and control them from anywhere with an internet connection.
- **Scalability**. Cloud infrastructure is highly scalable, meaning it can handle a large number of IoT devices and a large volume of data without requiring additional hardware or maintenance.
- **Reliability**. Cloud providers typically have robust infrastructure and support, which can make it easier to ensure that IoT devices are always connected and working properly.

You'll explore several ways to route or process messages in the cloud. In this tutorial, you'll use IoT Hub's built-in Event Hub endpoint to read the message from your device as detailed in the following diagram:

1. You start your event hub listener console application `d2ceventhublistener` and let it run in the background.
1. You start your `d2csendmsg` console application and send a message to the cloud.
1. Your `d2csendmsg` console application sends a message to IoT Hub.
1. Iot Hub queues the message into its built-in event hub.
1. Your `d2ceventhublistener` event hub client is notified that a new message is in the queue.
1. Your `d2ceventhublistener` retrieves the message queue position from storage.
1. Your `d2ceventhublistener` event hub client retrieves the message from the event hub queue and prints the message in your console application.

![lnk_sendmessage]

## Prerequisites

Completed the [Tutorial: Send a Message from the Cloud to a Simulated Device](tutorial-cloudtodevicemsg.md)

## Create a Message Listener for IoT Hub's Built-in Event Hub Endpoint

1. From Visual Studio Code, create a new file called `d2ceventhublistener.py`.
1. Copy and paste the following import statements into your `d2ceventhublistener.py` file

    ```python
    import asyncio
    import os
    from datetime import datetime
    from azure.eventhub.aio import EventHubConsumerClient
    from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
    ```

1. Copy and paste the following event handler after your import statements

    ```python
    async def on_event(partition_context, event):
        # Print the event data.
        print("[{0}] msg received: \"{1}\"".format(datetime.utcnow().isoformat(), event.body_as_str(encoding='UTF-8')))
    
        # Update the checkpoint for next read.
        await partition_context.update_checkpoint(event)
    ```

1. Copy and paste the following main function after your event handler. [todo] how to guide to obtain the connection strings.

    ```python
    async def main():
        # Create an Azure blob checkpoint store to store the checkpoints.
        checkpoint_store = BlobCheckpointStore.from_connection_string(os.getenv("STORAGE_CONNECTION_STRING"), os.getenv("STORAGE_CONTAINER_NAME"))
    
        # Create a consumer client for the event hub.
        client = EventHubConsumerClient.from_connection_string(os.getenv("EVENTHUB_CONNECTION_STRING"), consumer_group="$Default", eventhub_name=os.getenv("EVENTHUB_NAME"), checkpoint_store=checkpoint_store)
        async with client:
            # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
            await client.receive(on_event=on_event,  starting_position="-1")
    
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    ```

1. Change to your cloned GitHub directory `various\python` and run the event hub listener.

    ```powershell
    python d2ceventhublistener.py
    ```

    For example,

    ```python
    PS C:\repos\various\python> python d2ceventhublistener.py
    C:\repos\various\python\d2ceventhublistener.py:28: DeprecationWarning: There is no current event loop
      loop = asyncio.get_event_loop()
    ```

## Device message

1. Create a new file called `d2csendmsg.py`.
1. Copy and paste the following import statements into your `d2csendmsg.py` file

    ```python
    import os
    from azure.iot.device import IoTHubDeviceClient, Message
    ```

1. Copy and paste the following code to create the device client

    ```python
    client = IoTHubDeviceClient.create_from_connection_string(os.getenv("IOTHUB_DEVICE_CONNECTION_STRING"))
    ```

1. Copy and paste the following code to create a message

    ```python
    msg = Message('{{ "payload":"{0}" }}'.format(input("message to send: ")))
    msg.content_type = 'application/json;charset=utf-8'
    ```

1. Copy and paste the following code to send the message to IoT Hub

    ```python
    client.send_message(msg)
    ```

1. Run the Visual Studio Code debugger and provide a simple text message.

    From the Visual Studio Debugger Terminal,

    ```powershell
    message to send: test me!
    ```

    From the python session running the d2ceventhublistener.py file,

    ```python
    [2022-12-05 00:11:10.230220] msg received: "{ "payload":"test me!" }"
    ```

## Reference

[Read device-to-cloud messages from the built-in endpoint](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-read-builtin)

## Next Steps

[Tutorial: Upload a file to the Cloud from your Device](tutorial-uploaddevicefile.md)

<!--Images-->

[lnk_sendmessage]: media/tutorial-devicetocloudmsg/sendmessage.png