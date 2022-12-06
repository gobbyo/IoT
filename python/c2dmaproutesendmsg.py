import os
import json
import uuid
import asyncio
from azure.iot.device import Message
from azure.iot.hub import IoTHubRegistryManager

async def main():
    conn_str = os.getenv("IOTHUB_CONNECTION_STRING")
    mapkey = os.getenv("MAP_KEY")
    
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(conn_str)

        deviceId = input("Device Id to process map request: ")
        maptype = input("'guidance' or 'route' map type: ")
        maxChargekWh = input("vehicle max charge in kWH (e.g. Tesla Model Y = 75): ")
        currentChargePercent = input("current charge %: ")
        waypoints = input("number of waypoints (2 or more): ")
        
        route = []
        i = 0
        while i < int(waypoints):
            route.append(input("waypoint {0}:".format(str(i))).replace(" ",""))
            i += 1

        props={}
        # optional: assign system properties
        props.update(messageId = str(uuid.uuid4().hex))
        props.update(correlationId = str(uuid.uuid4().hex))

        props.update(key = mapkey)
        props.update(maptype = maptype)
        props.update(maxChargekWh = str(maxChargekWh))
        props.update(currentChargePercent = str(currentChargePercent))

        print(json.dumps(route)) 
        registry_manager.send_c2d_message(deviceId, json.dumps(route), props)

        input("Message sent, press Enter to continue...\n")

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    asyncio.run(main())