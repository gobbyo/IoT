import asyncio
import sys
import os
import time
import azure.maps.route.models
from azure.core.credentials import AzureKeyCredential
from azure.maps.route import MapsRouteClient

from azure.iot.device.aio import IoTHubDeviceClient

def message_handler(message):
    print("Message received:")
    key = ''
    data = []

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        if property[0] == 'custom_properties':
            for cprops in property[1].items():
                if cprops[0] == "key":
                    print("key={0}".format(cprops[1]))
                    key = cprops[1]
                elif cprops[0] == "userId":
                    print("userId={0}".format(cprops[1]))
                elif cprops[0] == "mapType":
                    print("mapType={0}".format(cprops[1]))
                else:
                    print ("    {}".format(cprops))
        elif property[0] == "data":
            print("data={0}".format(property[1]))
            s = str(property[1]).replace('b','')
            s = s.replace("\'","")
            route = s.split(':')
            start = route[0].split(',')
            end = route[1].split(',')
            data = [azure.maps.route.models.LatLon(start[0],start[1]),azure.maps.route.models.LatLon(end[0],end[1])]

        else:
            print ("    {}".format(property))
    
    if(len(key) > 1):
        if(len(data) > 1):
            route_summary(key,data)

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

def route_summary(key,routepoints):
    credential = AzureKeyCredential(key)

    client = MapsRouteClient(
        credential=credential
    )

    result = client.get_route_directions(route_points=routepoints, travel_mode='car', instructions_type="text", vehicle_engine_type='electric', compute_travel_time='all', constant_speed_consumption_in_kw_h_per_hundred_km='50,8.2:130,21.3', current_charge_in_kw_h='80', max_charge_in_kw_h='80')
    i = 0
    print("---------")
    total = len(result.routes[0].guidance.instructions)
    while i < total:
        if(result.routes[0].guidance.instructions[i].message == 'None'):
            if(i < total-1):
                print("{0}, then drive for {1} meters".format(result.routes[0].guidance.instructions[i].combined_message, result.routes[0].guidance.instructions[i+1].route_offset_in_meters - result.routes[0].guidance.instructions[i].route_offset_in_meters))
            else:
                print(result.routes[0].guidance.instructions[i].combined_message)
        else:
            if(i < total-1):
                print("{0}, then drive for {1} meters".format(result.routes[0].guidance.instructions[i].message, result.routes[0].guidance.instructions[i+1].route_offset_in_meters - result.routes[0].guidance.instructions[i].route_offset_in_meters))
            else:
                print(result.routes[0].guidance.instructions[i].message)
        i += 1
    print("---------")

if __name__ == "__main__":
    asyncio.run(main())