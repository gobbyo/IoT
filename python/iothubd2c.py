import asyncio
import sys
import os

from azure.iot.device.aio import IoTHubDeviceClient

async def main():
    # Fetch the connection string from an environment variable
    if len(sys.argv) != 2:
        exit

    conn_str = sys.argv[1]

    # Create instance of the device client using the authentication provider
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    curdir = os.path.dirname(os.path.realpath(__file__))
    with open(curdir + "\data.json","r") as data:
        list = []
        list = data.readlines()
        i = 0
        while i < len(list):
            # Send a single message
            await device_client.send_message(list[i])
            print("Message successfully sent: {0}".format(list[i]))
            i += 1
            await asyncio.sleep(1)

    # finally, shut down the client
    await device_client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())