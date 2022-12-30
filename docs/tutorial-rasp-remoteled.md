---
title: Remotely Control an LED 
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Remotely Control an LED

In this tutorial, you learn how to:

- Connect your Raspberry Pi to IoT Hub using the Device Provisioning Service
- Use custom properties to set the LED
- Receive a remote command and use the message custom properties to set the LED state

Following the diagram below.

![lnk_ledremotemsg]

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- Completed the tutorial to [Configure your Windows Machine](tutorial-configure.md)
- Completed the tutorial to [Connect and configure your Raspberry Pi with Visual Studio Code](tutorial-rasp-connect.md)

## Code your Raspberry Pi to Receive Messages to Light the LED

1. [Connect to your Raspberry Pi](https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host) using Visual Studio Code.
1. Create a file `remoteled.py` and save it in the `python/rasberrypi` directory from your GitHub clone, for example `~/repos/various/python/raspberrypi/remoteled.py`
1. Copy and paste the following import statements into your `remoteled.py` file.

    ```python
    import RPi.GPIO as GPIO
    import asyncio
    import time
    from decouple import config
    from azure.iot.device import Message, X509
    from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient
    ```

1. Copy and paste the following environment variables to access the Device Provisioning Service. Note the `DPS_HOST`, `DPS_SCOPEID`, and `DPS_REGISTRATIONID` will need to be added to the .env file, see the following table for details.

    ```python
    LED_channel = 17
    provisioning_host = config("DPS_HOST")
    id_scope = config("DPS_SCOPEID")
    registration_id = config("DPS_REGISTRATIONID")
    ```

    | **Connection Variable Name**  | **Value Found in portal.azure.com**  | **Details about finding the value**  |
    |:---------|:---------|:---------|
    | DPS_HOST | Device Provisioning Service > Overview > Service Endpoint | For example, "dpsztputik7h47qi.azure-devices-provisioning.net" |
    | DPS_SCOPEID | Device Provisioning Service > Overview > ID Scope | For example, "0ne008D45AC" |
    | DPS_REGISTRATIONID | Device Provisioning Service > Settings > Manage enrollments > Individual Enrollments | This is the value you provided in the tutorial [Create a x509 Certificate and Enroll Your Device](tutorial-dpsx509deviceenrollment.md) |

1. Copy and paste the following function. Note the code `message.custom_properties['LED']` gets the LED value of `On` or `Off`.

    ```python
    def message_handler(message):
        print("--Message Received--")
        try:
            s = message.custom_properties['LED']
            if s == 'On':
                GPIO.output(LED_channel, GPIO.HIGH)
                print("On")
            else:
                GPIO.output(LED_channel, GPIO.LOW)
                print("Off")
        finally:
            print("--Message Processed--")
    ```

1. Copy and paste the main function. You should be familiar with all the code as presented in previous tutorials.

    ```python
    async def main():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_channel, GPIO.OUT)
        GPIO.output(LED_channel, GPIO.LOW)
    
        print("Ctrl-C to quit'")
        print("Creating x509 cert object from file. Code id = e28c4236-60bb-4d45-adad-2a1b5cd0302e")
        x509 = X509(
            cert_file=config("X509_CERT_FILE"),
            key_file=config("X509_KEY_FILE"),
            pass_phrase=config("X509_PASS_PHRASE"),
        )
    
        print("Creating provisioning client from certificate. Code id = 7dc43b15-f17b-4f17-9446-8d26b1e188d2")
        provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
            provisioning_host=provisioning_host,
            registration_id=registration_id,
            id_scope=id_scope,
            x509=x509,
        )
    
        print("Registering provisioning client. Code id = 4d906cc4-61a9-4fe2-ab6e-4e397f63a702")
        registration_result = await provisioning_device_client.register()
    
        if registration_result.status == "assigned":
            device_client = IoTHubDeviceClient.create_from_x509_certificate(
                x509=x509,
                hostname=registration_result.registration_state.assigned_hub,
                device_id=registration_result.registration_state.device_id,
            )
    
        print("Connecting client to IoT hub. Code id = 6893e706-291e-44f5-8623-fea84046866a")
        await device_client.connect()
    
        device_client.on_message_received = message_handler
    
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            print("Program shut down by user")
        finally:
            GPIO.cleanup()
            await device_client.shutdown()
            print("Cleaning up and shutting down")
    
    if __name__ == "__main__":
        asyncio.run(main())
    ```

1. Run the program on your Raspberry Pi from Visual Studio Code.

    ```python
    $ ~/repos/various $ /bin/python /home/me/repos/various/python/raspberrypi/remoteled.py
    /home/me/repos/various/python/raspberrypi/remoteled.py:28: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
      GPIO.setup(LED_channel, GPIO.OUT)
    Ctrl-C to quit'
    Creating x509 cert object from file. Code id = e28c4236-60bb-4d45-adad-2a1b5cd0302e
    Creating provisioning client from certificate. Code id = 7dc43b15-f17b-4f17-9446-8d26b1e188d2
    Registering provisioning client. Code id = 4d906cc4-61a9-4fe2-ab6e-4e397f63a702
    Connecting client to IoT hub. Code id = 6893e706-291e-44f5-8623-fea84046866a
    ```

## Send a Remote Command to Turn the LED on and off
<!-- Introduction paragraph -->

1. From your windows machine, create a file `c2dsendmsg.py` in your cloned GitHub under the `python/raspberrypi` directory, for example `c:\repos\various\python\c2dsendmsg.py`
1. Copy and paste the following import statement

    ```python
    from uuid import uuid4
    from azure.iot.hub import IoTHubRegistryManager
    import os
    ```

1. Copy and paste the following main function to send a message to your device from the cloud.

    ```python
    def main():
        deviceId = input("Device id: ")
        s = input("On or Off: ")
        # Add any json to the payload as the content type is set to json
        payload = '{ "remote call": "Update LED" }'
        props={}
    
        try:
            registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))
            
            # assign system properties
            props.update(messageId = "{0}".format(uuid4()))
            props.update(contentType = "application/json")
            # assign 
            props.update(LED = s)
    
            registry_manager.send_c2d_message(deviceId, payload, props)
        except Exception as ex:
            print ( "Unexpected error {0}" % ex )
    
    if __name__ == "__main__":
        main()
    ```

<!-- Introduction paragraph -->
1. Run the program from Visual Studio Code, provide your device id, then type 'On' when prompted in the `TERMINAL`. For example,

    ```azurecli
    PS C:\repos\various> & C:/Users/me/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/repos/various/python/c2dsendmsg.py
    Device id: raspberrypi2
    On or Off: On
    ```

1. Verify your LED turns on when prompted and note the print statement from the code running on your Raspberry Pi.  For example,

    ```azurecli
    --Message Received--
        On
    --Message Processed--
    ```

## Next steps

Advance to the next article to learn how to create...
> [!div class="nextstepaction"]
> [Next steps button](contribute-how-to-mvc-tutorial.md)

<!--images-->

[lnk_ledremotemsg]: media/tutorial-rasp-remoteled/ledremotemsg.png
