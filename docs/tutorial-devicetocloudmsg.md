---
title: Send a Message from a Simulated Device To the Cloud
description: Tutorial to create device code that sends a message to the Cloud and code to send a message to a simulated Device from the Cloud
author: jbeman@hotmail.com
---

# Tutorial: Send a Message from a Simulated Device To the Cloud

In this tutorial, you learn how to:

- Create device code that sends a message to the Cloud
- Send a Message to your Simulated Device from the Cloud

There are several reasons to have an **IoT device send messages to the cloud**:

- *Data storage*. The cloud can provide a centralized location to store data collected from IoT devices. This data can then be used for a variety of purposes, such as analytics, machine learning, and more.
- *Remote access*. By sending data to the cloud, IoT devices can allow users to access and control them from anywhere with an internet connection.
- *Scalability*. Cloud infrastructure is highly scalable, meaning it can handle a large number of IoT devices and a large volume of data without requiring additional hardware or maintenance.
- *Reliability*. Cloud providers typically have robust infrastructure and support, which can make it easier to ensure that IoT devices are always connected and working properly.

In subsequent tutorials, you'll explore several ways to route or process messages in the cloud. In this tutorial, you'll start with IoT Hub's built-in Event Hub endpoint to read the message from your device as detailed in the following diagram:

1. Code and start your event hub listener console application `d2ceventhublistener` and let it run in the background.
1. Code and create a `d2csendmsg` console application.
1. Start your `d2csendmsg` console application and send a message to the cloud.
1. Iot Hub queues the message into its built-in event hub.
1. Your `d2ceventhublistener` event hub client is notified that a new message is in the queue.
1. Your `d2ceventhublistener` retrieves the message queue position from storage.
1. Your `d2ceventhublistener` event hub client retrieves the message from the event hub queue and prints the message in your console application.

![lnk_sendmessage]

An **event hub** is a real-time, distributed data streaming platform. It is designed to process and transmit large volumes of data from multiple sources simultaneously. There are several reasons to use an event hub:

- *Scalability*. An event hub is highly scalable and can handle millions of events per second, making it a good choice for handling large volumes of data from IoT (Internet of Things) devices or other sources.
- *Real-time processing*. An event hub allows you to process data in real-time, as it is generated. This can be useful for scenarios where you need to take action based on the data as soon as it is available.
- *Integration with other Azure services*. An event hub can be easily integrated with other Azure services, such as Azure Stream Analytics, Azure Functions, and Azure Machine Learning, which can be useful for processing and analyzing data in real-time.
- *Decoupling*. An event hub can help to decouple the producer of data from the consumer, allowing them to operate independently of each other. This can make it easier to scale and manage the overall system.

The communication across services like between the listener you'll create in this tutorial and the Event hub, rely on queues to process incoming messages. There are several reasons to **use a queue to store messages** for processing.

- *Load balancing*. A queue can act as a buffer between a producer of data (such as an IoT device) and a consumer of data (such as a backend system). This can help to balance the load between the producer and consumer, ensuring that the producer is not overwhelmed by the consumer.
- *Asynchrony*. A queue allows the producer and consumer of data to operate asynchronously, meaning they do not need to be running at the same time. This can be useful for scenarios where the consumer may not always be available to process data, or where the producer generates data at a faster rate than the consumer can handle.
- *Resilience*. A queue can store messages persistently, which means they are not lost if the consumer is unavailable or if there is a failure. This can help to make the overall system more resilient and robust.
- *Scaling*. A queue can scale horizontally, which means it can easily handle a large volume of messages without requiring additional infrastructure. This can be useful for scenarios where the volume of data from the producer varies over time.

## Prerequisites

Completed the [Tutorial: Send a Message from the Cloud to a Simulated Device](tutorial-cloudtodevicemsg.md)

## Create a Message Listener for IoT Hub's Built-in Event Hub Endpoint

In this section you'll use the Event Hub consumer client to access queued messages in the IoT Hub's built-in Event Hub.

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

1. Change to your cloned GitHub directory `IoT\python` and run the event hub listener.

    ```powershell
    python d2ceventhublistener.py
    ```

    For example,

    ```python
    PS C:\repos\vusingarious\python> python d2ceventhublistener.py
    C:\repos\IoT\python\d2ceventhublistener.py:28: DeprecationWarning: There is no current event loop
      loop = asyncio.get_event_loop()
    ```

## Device message

In this section you'll create code to send a message from your device directly to IoT Hub using a device connection string. While storing the IoT Hub's connection string on your device is easy and convenient, it is generally not a good practice because your device is connected directly to the IoT Hub instance which doesn't scale without migrating your device and it could go offline at any time. In future tutorials we'll use the Device Provisioning Service to connect to IoT Hub rather than storing the IoT Hub connection string on your device.

1. Create a new file called `d2csendmsg.py` in your `{forked github}\python` directory, e.g. `c:\repos\IoT\python`.
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