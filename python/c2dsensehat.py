import asyncio
import time
import json
from decouple import config
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient

def message_handler(message):
    print("--Message Received--")
    print("payload={data}".format(data=Message(message).data))
    json.loads(Message(message).data)
    print("payload (json)={data}".format(data=json.dumps()))

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