# Device sends a message to IoT Hub

In this tutorial you'll create device code that sends a message to IoT Hub.

[todo] image needed

## Prerequisites

[todo]

## Create a message listener for IoT Hub

1. From Visual Studio Code, create a new file called `d2ceventhublistener.py`.
1. Copy and paste the following import statements into your `d2ceventhublistener.py` file

    ```python
    import asyncio
    import os
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

1. Open a separate PowerShell session and run the following scripts to set your machine environment variables in a terminal session in Visual Studio Code.  Replace the `{Storage Account > Access Keys > Connection String}` and `{Storage Account > Containers > Name}` using the storage account you created with your IoT Hub. See the article to [Manage storage account access keys](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/storage/common/storage-account-keys-manage.md#manage-storage-account-access-keys) for details. Replace the `{IoT Hub > Built-in endpoints > Event Hub-compatible endpoint}` and `{IoT Hub > Built-in endpoints > Event Hub-compatible name}` using the IoT Hub instance you created, see the article [Read from the built-in endpoint](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messages-read-builtin#read-from-the-built-in-endpoint) for details.

    ```powershell
    $Env:STORAGE_CONNECTION_STRING="{Storage Account > Access Keys > Connection String}"
    $Env:STORAGE_CONTAINER_NAME="{Storage Account > Containers > Name}"
    $Env:EVENTHUB_CONNECTION_STRING="{IoT Hub > Built-in endpoints > Event Hub-compatible endpoint}"
    $Env:EVENTHUB_NAME="{IoT Hub > Built-in endpoints > Event Hub-compatible name}"
    ```

    For example,

    ```powershell
    $Env:STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=hubmsgw2lu5yeop2qwy;AccountKey=P2X2******g==;EndpointSuffix=core.windows.net"
    $Env:STORAGE_CONTAINER_NAME="hubmsgresults"
    $Env:EVENTHUB_CONNECTION_STRING="Endpoint=sb://ihsuproddmres006dednamespace.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=W+tl*******QXM=;EntityPath=iothub-ehub-hubmsghubw-23135425-309430d575"
    $Env:EVENTHUB_NAME="iothub-ehub-hubmsghubw-23135425-309430d575"
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
