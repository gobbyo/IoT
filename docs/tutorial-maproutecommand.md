# Device Map Route Listener

In this tutorial you'll create device that listens to a command to calculates an prints the instructions for a map route.

[todo] image needed

## Prerequisites

[todo]

## Send a Map Command to your Map Device

1. Create a new file called `c2dmaproutesendmsg.py`.
1. Copy and paste the following import statements into your `c2dmaproutesendmsg.py` file

    ```python
    import os
    import json
    import uuid
    import asyncio
    from azure.iot.hub import IoTHubRegistryManager
    ```

1. Copy and paste the following code to create the device client

    ```python
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
    ```

1. Run the Visual Studio Code debugger and [todo: complete this section]

## Reference

- IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)
