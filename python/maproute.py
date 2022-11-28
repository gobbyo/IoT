import os
import string
import json
import sys
import azure.maps.route.models
from azure.core.credentials import AzureKeyCredential
from azure.maps.route import MapsRouteClient

#listOfLatLon = listOfLatLon.append('47.61796662516246, -121.949074626174'), listOfLatLon.append('47.647353510681015, -121.91641447009559'), etc.
def createRouteList(listOfLatLon):
    latlonroute = []
    i = 0
    while i < len(listOfLatLon):
        point = listOfLatLon[i].split(',')
        latlonroute.append( azure.maps.route.models.LatLon(point[0].replace(' ',''),point[1].replace(' ','')))
        i += 1
    return latlonroute

#mapkey: Azure Maps authentication primary key
#route: list of LatLon
#filepath: writes json snippets to file if exists
def printRouteOfLatLon(mapkey,route,filepath):
    credential = AzureKeyCredential(mapkey)

    client = MapsRouteClient(
        credential=credential
    )

    result = client.get_route_directions(route_points=route, 
    travel_mode="car", instructions_type="text", route_type="shortest", vehicle_engine_type="electric", compute_travel_time="all",
    constant_speed_consumption_in_kw_h_per_hundred_km="50,8.2:130,21.3", current_charge_in_kw_h=80, max_charge_in_kw_h=80)

    print("--Route LatLon List--")

    pt = 0
    leg = 0

    if(os.path.exists(filepath)):
        with open(filepath,"w") as fp:
            while leg < len(result.routes[0].legs):
                while pt < len(result.routes[0].legs[leg].points):
                    fp.write("{" + "{0}, {1}".format(str(result.routes[0].legs[0].points[pt].latitude), str(result.routes[0].legs[0].points[pt].longitude)) + "}\n")
                    pt += 1
                leg += 1

        fp.close()
    else:
        while leg < len(result.routes[0].legs):
            while pt < len(result.routes[0].legs[leg].points):
                print("{lat:" + str(result.routes[0].legs[0].points[pt].latitude) + ",lon:" + str(result.routes[0].legs[0].points[pt].longitude) + "}")
                pt += 1
            leg += 1

#guidance: see Azure map result.routes[].guidance
#i: index of guidance.instructions
#total: total guidance.instructions
def guidanceInstructions(guidance, i, total):
    s = ''
    count = ''
    if(i==0):
        count = 'START'
    elif (i==total-1):
        count = 'END'
    else:
        count = i

    if(guidance.instructions[i].message == 'None'):
        if(i < total-1):
            s = "{0}. {1}, then drive for {2} meters".format(count, guidance.instructions[i].combined_message, guidance.instructions[i+1].route_offset_in_meters - guidance.instructions[i].route_offset_in_meters)
        else:
            s = "{0}. {1}".format(count, guidance.instructions[i].combined_message)
    else:
        if(i < total-1):
            s = "{0}. {1}, then drive for {2} meters".format(count, guidance.instructions[i].message, guidance.instructions[i+1].route_offset_in_meters - guidance.instructions[i].route_offset_in_meters)
        else:
            s = "{0}. {1}".format(count, guidance.instructions[i].message)
    return s

#mapkey: Azure Maps authentication primary key
#route: list of LatLon
#filepath: writes to file if exists
def printRouteGuidanceLatLon(mapkey,route,filepath):
    
    credential = AzureKeyCredential(mapkey)

    client = MapsRouteClient(
        credential=credential
    )

    result = client.get_route_directions(route_points=route, 
    travel_mode="car", instructions_type="text", route_type="shortest", vehicle_engine_type="electric", compute_travel_time="all",
    constant_speed_consumption_in_kw_h_per_hundred_km="50,8.2:130,21.3", current_charge_in_kw_h=80, max_charge_in_kw_h=80)
    
    print("--Route Guidance--")

    i = 0
    total = len(result.routes[0].guidance.instructions)

    if(os.path.exists(filepath)):
        with open(filepath, 'w') as fp:
            while i < total:
                fp.write(guidanceInstructions(result.routes[0].guidance, i, total) + "\n")
                i += 1
        fp.close()
    else:
        while i < total:
            print(guidanceInstructions(result.routes[0].guidance, i, total))
            i += 1
