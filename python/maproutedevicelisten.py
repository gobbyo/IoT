import asyncio
import sys
import os
import time
import pickle
import azure.maps.route.models
from azure.core.credentials import AzureKeyCredential
from azure.maps.route import MapsRouteClient
from maproute import createRouteList, printRouteOfLatLon, printRouteGuidanceLatLon

from azure.iot.device.aio import IoTHubDeviceClient

def message_handler(message):
    print("Message Received")
    mapkey = ''
    maptype = ''
    data = []

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        if property[0] == 'custom_properties':
            for cprops in property[1].items():
                if cprops[0] == "key":
                    mapkey = cprops[1]
                    print("\tkey={0}".format(mapkey))
                elif cprops[0] == "maptype":
                    maptype = cprops[1]
                    print("\tmaptype={0}".format(maptype))
        elif property[0] == "data":
            data = pickle.loads(property[1])
            print("\tdata={0}".format(data)) 
    
    if(maptype == 'guidance'):
        if(len(mapkey) > 1):
            if(len(data) > 1):
                printRouteGuidanceLatLon(mapkey,createRouteList(data),'')
    elif(maptype == 'route'):
        if(len(mapkey) > 1):
            if(len(data) > 1):
                printRouteOfLatLon(mapkey,createRouteList(data),'')
    else:
        print('unknown map type, choose \"route\" or \"guidance\"')

async def main():
    if len(sys.argv) != 2:
        exit

    conn_str = sys.argv[1]

    client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    print ("...waiting for C2D messages, press Ctrl-C to exit.")
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