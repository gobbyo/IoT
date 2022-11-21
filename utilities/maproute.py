import os
import string
import json
import sys
from azure.core.credentials import AzureKeyCredential
from azure.maps.route import MapsRouteClient

# Fetch the connection string as an arg
if len(sys.argv) != 2:
    exit

credential = AzureKeyCredential(sys.argv[1])

client = MapsRouteClient(
    credential=credential
)

fp = open("data.json","w")
result = client.get_route_directions(route_points=[(48.503364324046956, -122.66808799216393), (47.245622, -122.429602)], 
travel_mode="car", vehicle_engine_type="electric", compute_travel_time="all",
constant_speed_consumption_in_kw_h_per_hundred_km="50,8.2:130,21.3", current_charge_in_kw_h=80, max_charge_in_kw_h=80)
i = 0
print(str(result.routes[0].summary))
print("---------")

while i < len(result.routes[0].legs[0].points):
    p = "{lat:" + str(result.routes[0].legs[0].points[i].latitude) + ",lon:" + str(result.routes[0].legs[0].points[i].longitude) + "}"
    print(p)
    fp.write(p + "\n")
    i += 1

fp.close()