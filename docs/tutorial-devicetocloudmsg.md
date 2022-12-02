# Device sends a message to IoT Hub

In this tutorial you'll create device code that sends a message to IoT Hub.

[todo] image needed

## Prerequisites

[todo]

## Create a message listener for IoT Hub

1. Create a new file called `d2ceventhublistener.py`.
1. Copy and paste the following import statements into your `d2ceventhublistener.py` file

    ```python
    import asyncio
    import sys
    import datetime
    from azure.eventhub.aio import EventHubConsumerClient
    from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
    ```

1. Copy and paste the following event handler after your import statements

    ```python
    async def on_event(partition_context, event):
        # Print the event data.
        print("[{0}] msg received: \"{1}\"".format(datetime.datetime.utcnow(), event.body_as_str(encoding='UTF-8')))
    
        # Update the checkpoint for next read.
        await partition_context.update_checkpoint(event)
    ```

1. Copy and paste the following main function after your event handler.

    ```python
    async def main():
        storageconnection = input("Storage connection string: ")
        blobcontainername = input("Storage container name: ")
        eventhubconnection = input("Built-in event hub route connection string: ")
        eventhubname = input("Built-in event hub name: ")
    
        # Create an Azure blob checkpoint store to store the checkpoints.
        checkpoint_store = BlobCheckpointStore.from_connection_string(storageconnection, blobcontainername)
    
        # Create a consumer client for the event hub.
        client = EventHubConsumerClient.from_connection_string(eventhubconnection, consumer_group="$Default", eventhub_name=eventhubname, checkpoint_store=checkpoint_store)
        async with client:
            # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
            await client.receive(on_event=on_event,  starting_position="-1")
    
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    ```

1. Run the listener. [todo] Add steps.

## Device sends a message to IoT Hub

1. Create a new file called `d2csendmsg.py`.
1. Copy and paste the following import statements into your `d2csendmsg.py` file

    ```python
    from azure.iot.device import IoTHubDeviceClient, Message
    ```

1. Copy and paste the following code to create the device client

    ```python
    client = IoTHubDeviceClient.create_from_connection_string(input("Device Connection String: "))
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

## Reference

- IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)