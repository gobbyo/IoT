# Send Hostname and IP address to the Cloud

In this tutorial you'll create device code that sends a message to IoT Hub. Knowing your Raspberry Pi's hostname and IP address is needed to connect via ssh or from Visual Studio Code.

[todo] image needed

## Prerequisites

[todo]

## Code a Message with your Device Hostname and IP Address to the Cloud

1. Create a new file called `d2cipandhostname.py`.
1. Copy and paste the following import statements into your `d2cipandhostname.py` file

    ```python
    import socket
    import time
    from datetime import datetime
    from decouple import config
    from azure.iot.device import IoTHubDeviceClient, exceptions
    ```

1. Copy and paste the following code after the import statements to get the IP address of your device

    ```python
    def get_ip_address():
        ip_address = ''
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("1.1.1.1",80))
            ip_address = s.getsockname()[0]
            s.close()
        except socket.error as e:
            print("Error: {0}. CodeID = 2e798e2d-0802-4b1d-9860-a83e3e35b599".format(e))
        return ip_address
    ```

1. Copy and paste the following code to create a message

    ```python
    def main():
        print("[{0}] Send IoT Hub this device's Host Name and IP address. CodeID = b5faac72-eee4-43fe-9af1-33b489c51add".format(datetime.utcnow().isoformat()))
        #wait 30 seconds for the system to get up and running after reboot
        time.sleep(30)
        try:
            hostname = socket.gethostname()
            ip_address = get_ip_address()
    ```

1. Copy and paste the following code within the `def main()` function to send the message to IoT Hub

    ```python
    msg = '{{ "Hostname":"{0}", "IPAddress":"{1}" }}'.format(hostname, ip_address)
    client = IoTHubDeviceClient.create_from_connection_string(config("IOTHUB_DEVICE_CONNECTION_STRING"))
    client.send_message(msg)
    ```

1. Copy and paste the following code within the `def main()` function to handle any exceptions and print activity to the command line

    ```python
    except exceptions.ClientError as e:
            print("Error: {0}. CodeID = 2f85db08-398e-4997-ab67-b9105a328e0e".format(e))
    finally:
        print("[{0}] Connection string: {1}. CodeID = 2b700d52-b1d2-41ad-8a78-90d59c9d083a".format(datetime.utcnow().isoformat(),config("IOTHUB_DEVICE_CONNECTION_STRING")))
        print("[{0}] Message sent: {1}".format(datetime.utcnow().isoformat(), msg))
    ```

1. Add the following code to start code execution with the main() function

    ```python
    if __name__ == "__main__":
        main()
    ```

1. Run the Visual Studio Code debugger or run the script from your command line.

    ```python
    python d2cipandhostname.py
    ```

    For example,

    ```python
    PS C:\repos\various\python\raspberrypi>  python d2cipandhostname.py
    [2022-12-21T05:06:51.616476] Get IP and Host Name. codeID = b5faac72-eee4-43fe-9af1-33b489c51add
    [2022-12-21T05:06:52.532383] Connection string: HostName=HubMsgHubw2lu5yeop2qwy.azure-devices.net;DeviceId=myDevice;SharedAccessKey=8IrOxxxxxxxxxxZUkg=. codeID = 2b700d52-b1d2-41ad-8a78-90d59c9d083a
    [2022-12-21T05:06:52.543905] Message sent: { "Hostname":"HJB34C6", "IPAddress":"192.168.86.86" }
    ```

## Set up a Cron job to Send the Message when your Raspberry Pi Boots

[todo]

## Verify the Message is Written to Blob Storage

[todo]

## Reference

- IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)
