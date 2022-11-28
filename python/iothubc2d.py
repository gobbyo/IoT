import random
import sys
from azure.iot.hub import IoTHubRegistryManager

MESSAGE_COUNT = 2
AVG_WIND_SPEED = 10.0
MSG_TXT = "{\"service client sent a message\": %.2f}"


def main():
    if len(sys.argv) != 3:
        exit

    conn_str = sys.argv[1]
    deviceId = sys.argv[2]

    try:
        print ("start location:")
        startLoc = input().replace(" ","")
        print ("end location:")
        endLoc = input().replace(" ","")

        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(conn_str)

        print ( 'Sending message: {0}'.format(i) )
        data = format("\{{0}:{1}\}", startLoc, endLoc)

        props={}
        # optional: assign system properties
        props.update(messageId = "message_%d" % i)
        props.update(correlationId = "correlation_%d" % i)
        props.update(contentType = "application/json")

        # optional: assign application properties
        prop_text = "PropMsg_%d" % i
        props.update(testProperty = prop_text)

        registry_manager.send_c2d_message(deviceId, data, properties=props)

        try:
            # Try Python 2.xx first
            raw_input("Press Enter to continue...\n")
        except:
            pass
            # Use Python 3.xx in the case of exception
            input("Press Enter to continue...\n")

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging service sample..." )

    iothub_messaging_sample_run()