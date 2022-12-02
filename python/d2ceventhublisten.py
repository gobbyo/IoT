import asyncio
import sys
import datetime
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore

async def on_event(partition_context, event):
    # Print the event data.
    print("[{0}] msg received: \"{1}\"".format(datetime.datetime.utcnow(), event.body_as_str(encoding='UTF-8')))

    # Update the checkpoint for next read.
    await partition_context.update_checkpoint(event)

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