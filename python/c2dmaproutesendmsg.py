import uuid
import sys
import asyncio
import pickle
from azure.iot.hub import IoTHubRegistryManager

async def main():
    if len(sys.argv) != 4:
        exit

    conn_str = sys.argv[1]
    deviceId = sys.argv[2]
    mapkey = sys.argv[3]
    
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(conn_str)

        maptype = input("'guidance' or 'route' map type:")
        maxChargekWh = input("vehicle max charge in kWH (e.g. Tesla Model Y = 75):")
        currentChargePercent = input("current charge %:")
        waypoints = input("number of waypoints (2 or more): ")
        
        route = []
        i = 0
        while i < int(waypoints):
            route.append(input("waypoint {0}:".format(str(i))).replace(" ",""))
            i += 1

        data = (pickle.dumps(route))

        props={}
        # optional: assign system properties
        props.update(messageId = str(uuid.uuid4().hex))
        props.update(correlationId = str(uuid.uuid4().hex))
        props.update(contentType = "application/json")

        props.update(key = mapkey)
        props.update(maptype = maptype)
        props.update(maxChargekWh = str(maxChargekWh))
        props.update(currentChargePercent = str(currentChargePercent))

        registry_manager.send_c2d_message(deviceId, data, properties=props)

        input("Message sent, press Enter to continue...\n")

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    asyncio.run(main())