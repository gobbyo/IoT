import asyncio
import time
from azure.iot.device import IoTHubDeviceClient

def message_handler(message):
    print("--Message Received--")
    print(message)

async def main():
    client = IoTHubDeviceClient.create_from_connection_string(input("IoT Hub *Device* Connection String:"))
    print("--Waiting for Messages--") 
    
    try:
        client.on_message_received = message_handler
        while True:
            #ctrl-c to exit
            await time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())