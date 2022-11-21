import asyncio
import sys
import datetime
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore

async def on_event(partition_context, event):
    # Print the event data.
    print("[{0}] msg received: \"{1}\"".format(datetime.datetime.utcnow(), event.body_as_str(encoding='UTF-8')))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    if len(sys.argv) != 5:
        exit

    blobstorageconnection = sys.argv[1]
    blobcontainername = sys.argv[2]
    eventhubconnection = sys.argv[3]
    eventhubname = sys.argv[4] 
    
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string(blobstorageconnection, blobcontainername)

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(eventhubconnection, consumer_group="$Default", eventhub_name=eventhubname, checkpoint_store=checkpoint_store)
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        await client.receive(on_event=on_event,  starting_position="-1")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())