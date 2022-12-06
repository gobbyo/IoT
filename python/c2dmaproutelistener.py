import asyncio
import sys
import time
import json
from azure.core.credentials import AzureKeyCredential
from azure.maps.route import MapsRouteClient
from maproute import createRouteList, printEVRoute, printEVRouteGuidance

from azure.iot.device.aio import IoTHubDeviceClient

def message_handler(message):
    print("Message Received")
    mapkey = ''
    maptype = ''
    currentChargePercent = 0.0
    data = []

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        if property[0] == 'custom_properties':
            for cprops in property[1].items():
                if cprops[0] == 'key':
                    mapkey = cprops[1]
                    print("\tkey={0}".format(mapkey))
                elif cprops[0] == 'currentChargePercent':
                    currentChargePercent = float(cprops[1]) * 0.01
                    print("\tcurrentChargePercent={0}".format(currentChargePercent*100))
                elif cprops[0] == 'maxChargekWh':
                    maxChargekWh = float(cprops[1])
                    print("\tmaxChargekWh={0}".format(maxChargekWh))
                elif cprops[0] == 'maptype':
                    maptype = cprops[1]
                    print("\tmaptype={0}".format(maptype))
        elif property[0] == "data":
            data = json.loads(property[1])
            print("\tdata={0}".format(data)) 
    
    if(maptype == 'guidance'):
        if(len(mapkey) > 1):
            if(len(data) > 1):
                printEVRouteGuidance(mapkey,createRouteList(data),'',currentChargePercent,maxChargekWh)
    elif(maptype == 'route'):
        if(len(mapkey) > 1):
            if(len(data) > 1):
                printEVRoute(mapkey,createRouteList(data),'',currentChargePercent,maxChargekWh)
    else:
        print('unknown map type, choose \"route\" or \"guidance\"')

async def main():
    conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

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