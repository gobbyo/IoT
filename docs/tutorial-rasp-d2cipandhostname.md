# Tutorial: Send Hostname and IP address to the Cloud

In this tutorial you'll create device code that sends a message to IoT Hub. Knowing your Raspberry Pi's hostname and IP address is needed to connect via ssh or from Visual Studio Code.

[todo] image needed

## Prerequisites

[Deploy and Configure StreamAnalytics](tutorial-deploystreamtostorage.md)

## Code a Message with your Device Hostname and IP Address to the Cloud

1. Create a new directory called `modules` under the `\various\python\raspberrypi\`, e.g. `\various\python\raspberrypi\modules`.
1. Create a new file called `raspipaddress.py` in the `\various\python\raspberrypi\modules` directory path you created in the previous step.
1. Copy and paste the following code into your `raspipaddress.py` file

    ```python
    import socket
    
    def get_ip_address():
        ip_address = ''
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("1.1.1.1",80))
            ip_address = s.getsockname()[0]
            s.close()
        except socket.error as e:
            print("Error: {0}. CodeID = {new-guid}".format(e))
        return ip_address
    ```

    This code uses a local socket connection to figure out your raspberry pi's public facing IP address.

1. Replace the `{new-guid}` by typing the following script in a PowerShell terminal from your Visual Studio Code.

    ```powershell
    new-guid
    ```

    For example,

    ```powershell
    PS> new-guid
    
    Guid
    ----
    afd02cb8-8984-496d-ad3f-151165cf8eaf
    ```

    Having a unique identifier in code helps you to troubleshoot should something go wrong in your code. Simply capture your print output into a file and search for the error that occurred by its unique code identifier.

1. Create a new file called `d2cipandhostname.py` and save it into your cloned github path `\various\python\raspberrypi\`.
1. Copy and paste the following import statements into your `d2cipandhostname.py` file

    ```python
    import asyncio
    import socket
    import uuid
    from decouple import config
    from azure.iot.device import Message,X509
    from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient
    import modules.raspipaddress as raspipaddress
    ```

1. Copy and paste the following variables you obtain from your .env file.

    ```python
    provisioning_host = config("DPS_HOST")
    id_scope = config("DPS_SCOPEID")
    registration_id = config("DPS_REGISTRATIONID")
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

1. Run the following command in your Raspberry Pi,

    ```azurecli
    $ sudo crontab -e
    ```

1. Add the following entry to cron,

    ```azurecli
    @reboot python ~/repos/various/python/raspberrypi/d2cipandhostname.py
    ```

1. Type ctrl-o and hit the enter key, for example,

    ```azurecli
    $ ctrl-o
    $ File Name to Write: /tmp/crontab.4SQV5b/crontab
    ```

1. Type `ctrl-x` to exit `crontab`, then run the following command,

    ```azurecli
    sudo shutdown -r
    ```

## Verify the Message from your Stream Analytics Jobs Service

1. Open your stream analytics jobs service using the [Azure portal](https://portal.azure.com).
1. Select `Job topology > <> Query` in the left pane and verify the message exists in the `Input preview` pane.
[todo]

## Reference

- IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)

## Next Steps

Congratulations, you've successfully remotely coded a real device and connected it to Azure! You are ready to continue your journey and learn to wire various electronics to your Raspberry Pi and remotely controlling it.

[Tutorial: Light up an LED](tutorial-rasp-led.md)
