# Send Sensor Hat Data to the Cloud

In this tutorial you'll create device code that sends a message to IoT Hub. Knowing your Raspberry Pi's hostname and IP address is needed to connect via ssh or from Visual Studio Code.

[todo] image needed

## Prerequisites

[todo]

## Code a Message with your Device Hostname and IP Address to the Cloud

1. Connect to your Raspberry Pi with Visual Studio Code's "Remote Explorer"
1. Create a new file called `d2csensorhat.py`.
1. Copy and paste the following import statements into your `d2csensorhat.py` file

    ```python
    from datetime import datetime
    from decouple import config
    from azure.iot.device import IoTHubDeviceClient
    from azure.iot.device import exceptions
    from sense_hat import SenseHat
    ```

1. Copy and paste the following code after the import statements to create and send the message to IoT Hub

    ```python
    def main():
        try:
            print("[{0}] Send IoT Hub this device's sense hat data. CodeID = 69203252-1954-4f68-ba9c-3c38301ba9e3".format(datetime.utcnow().isoformat()))
            sense = SenseHat()
            client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))
            f = (sense.temperature * 9/5) + 32
            msg = '{ "sent_utc":"%sZ", "fahrenheit":"%3.0f", "humidity":"%3.0f", "pressure":"%3.0f" }'%(datetime.utcnow().isoformat(),f,sense.humidity,sense.pressure)
            client.send_message(msg)
        except exceptions.ClientError as e:
            print("Error: {0}. CodeID = fb3c2792-cf4c-4249-825e-f2d8bceade23".format(e))
        finally:
            # Graceful exit
            print("[{0}] Message sent: {1}. CodeID = 49a71765-7203-45f5-abc7-a559ac91d818".format(datetime.utcnow().isoformat(), msg))
            print(msg)
            sense.clear()
    
    if __name__ == "__main__":
        main()
    ```

1. Run the Visual Studio Code debugger or run the script from your command line.

    ```python
    python d2csensorhat.py
    ```

## Set up a Cron job to Send the Message on a schedule from your Raspberry Pi

[todo]

## Verify Messages are Written to Blob Storage

[todo]

## Reference

- IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)
