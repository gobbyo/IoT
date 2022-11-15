from azure.eventhub import EventHubConsumerClient

connection_str = 'Endpoint=sb://jbemaneventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=lLlTjF0jdW6sgGMD7/1qGQ7k2S9bNemnQl5Flc1mWco='
consumer_group = '$Default'
eventhub_name = 'jbemanEventHub'
client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)
partition_ids = client.get_partition_ids()
print(partition_ids)