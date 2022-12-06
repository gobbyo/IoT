# Device Map Route Listener

In this tutorial you'll create device that listens to a command to calculates an prints the instructions for a map route.

[todo] image needed

## Prerequisites

[todo]

## Create a map listener for IoT Hub

1. From Visual Studio Code, create a new file called `c2dmaproutelistener.py`.
1. Copy and paste the following import statements into your `c2dmaproutelistener.py` file

    ```python
    import os
    import time
    import json
    import asyncio
    from azure.core.credentials import AzureKeyCredential
    from azure.maps.route import MapsRouteClient
    from maproute import createRouteList, printEVRoute, printEVRouteGuidance
    from azure.iot.device.aio import IoTHubDeviceClient
    ```

1. Copy and paste the following event handler after your import statements

    ```python
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
    ```

1. Copy and paste the following main function after your event handler.

    ```python
    async def main():
        client = IoTHubDeviceClient.create_from_connection_string(os.getenv("IOTHUB_DEVICE_CONNECTION_STRING"))
    
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
    ```
