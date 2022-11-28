import uuid
import sys
import asyncio
from azure.iot.hub import IoTHubRegistryManager

async def main():
    if len(sys.argv) != 3:
        exit

    conn_str = sys.argv[1]
    deviceId = sys.argv[2]

    try:
        uniqueuserId = input("your user ID:")
        mapkey = input("subscription key to map service:")
        startLoc = input("start location:").replace(" ","")
        endLoc = input("end location:").replace(" ","")

        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(conn_str)

        data = ("{0}:{1}").format(startLoc,endLoc)

        props={}
        # optional: assign system properties
        props.update(messageId = str(uuid.uuid4().hex))
        props.update(correlationId = str(uuid.uuid4().hex))
        props.update(contentType = "application/json")

        props.update(key = str(mapkey))
        props.update(userId = str(uniqueuserId))
        props.update(mapType = "route")

        registry_manager.send_c2d_message(deviceId, data, properties=props)

        input("Message sent, press Enter to continue...\n")

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging service sample..." )
    asyncio.run(main())