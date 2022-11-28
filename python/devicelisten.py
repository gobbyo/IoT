import asyncio
import sys
import os
import time

from azure.iot.device.aio import IoTHubDeviceClient

def message_handler(message):
    print("Message received:")

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        print ("    {}".format(property))

async def main():
    if len(sys.argv) != 2:
        exit

    conn_str = sys.argv[1]
    print ("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = message_handler

        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())