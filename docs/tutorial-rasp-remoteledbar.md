---
title: Remotely Control an LED Display Bar
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Remotely Control an LED Display Bar

In this tutorial, you learn how to:

- Connect your Raspberry Pi to IoT Hub using the Device Provisioning Service
- Use custom properties to set the LED
- Receive a remote command and use the message custom properties to set the LED state

In the [Tutorial: Remotely Control an LED](tutorial-rasp-remoteled.md) you remote controlled the LED using the message property. In this tutorial we'll explore sending a payload that describes more than the simple state of being "on" or "off". Following the diagram below.

1. You'll use Visual Studio Code to remotely connect to your Raspberry Pi and create listener code to receive messages and change the state of the LED display bar.
1. When you start the code, your Raspberry Pi will use the Device Provisioning Service to create an IoT device client.
1. You'll use the IoT device client to connect to IoT Hub and await for incoming messages.
1. You'll use a local instance of Visual Studio Code to send a message to your Raspberry Pi.
1. The listener program receives the incoming message.
1. The listener program reads the message payload then animates the LED display bar accordingly.

    ![lnk_remoteledbar]

## Prerequisites

- Completed the [Tutorial: Light up an LED bar](tutorial-rasp-ledbar.md)

## Code your Raspberry Pi to Receive Messages to Light the LED

1. [Remotely connect to your Raspberry Pi](tutorial-rasp-connect.md#set-up-remote-ssh-with-visual-studio-code).
1. Create a file `remoteledbar.py` and save it in the `python/rasberrypi` directory from your GitHub forked clone, for example `~/repos/IoT/python/raspberrypi/remoteledbar.py`. This is a message listener program that runs on your Raspberry Pi.
1. Copy and paste the following import statements into your `remoteledbar.py` file.

    ```python
    import RPi.GPIO as GPIO
    import asyncio
    import time
    import json
    from decouple import config
    from azure.iot.device import Message, X509
    from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient
    ```

1. Copy and paste the following variables following your import statements from the previous step. Note the `DPS_HOST`, `DPS_SCOPEID`, and `DPS_REGISTRATIONID` will need to be added to your [`.env` file](howto-connectionstrings.md), see the following table for details.

    ```python
    LED_pins = [8,12,16,18,22,24,26,32,36,38]
    provisioning_host = config("DPS_HOST")
    id_scope = config("DPS_SCOPEID")
    registration_id = config("DPS_REGISTRATIONID")
    ```

    | **Connection Variable Name**  | **Value Found in portal.azure.com**  | **Details about finding the value**  |
    |:---------|:---------|:---------|
    | DPS_HOST | Device Provisioning Service > Overview > Service Endpoint | For example, "dpsztputik7h47qi.azure-devices-provisioning.net" |
    | DPS_SCOPEID | Device Provisioning Service > Overview > ID Scope | For example, "0ne008D45AC" |
    | DPS_REGISTRATIONID | Device Provisioning Service > Settings > Manage enrollments > Individual Enrollments | This is the value you provided in the tutorial [Create a x509 Certificate and Enroll Your Device](tutorial-dpsx509deviceenrollment.md) |

1. Copy and paste the following function. Note the code reads the message payload data to determine the LED bar lighting order and the wait time between changing the LED state.

    ```python
    def message_handler(message):
        print("--Message Received--")
        try:
            payload = json.loads(message.data)
            seq = list(payload['order'])
            pause = float(payload['pause'])
    
            for s in seq:
                print("pin:{0}, state:{1}".format(LED_pins[int(s)], payload['state']))
    
                if payload['state'] == 'on':
                    GPIO.output(LED_pins[int(s)], GPIO.HIGH)
                else:
                    GPIO.output(LED_pins[int(s)], GPIO.LOW)   
                time.sleep(pause)
    
        finally:
            print("--Message Processed--")
    ```

1. Copy and paste the main function. You should be familiar with all the code as presented in previous tutorials.

    ```python
    async def main():
        GPIO.setmode(GPIO.BOARD)
    
        for p in LED_pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, GPIO.LOW)
    
        print("Ctrl-C to quit'")
        print("Creating x509 cert object from file. Code id = 3a931dc7-9028-409f-be9f-7065fe6de8eb")
        x509 = X509(
            cert_file=config("X509_CERT_FILE"),
            key_file=config("X509_KEY_FILE"),
            pass_phrase=config("X509_PASS_PHRASE"),
        )
    
        print("Creating provisioning client from certificate. Code id = 53503ead-4f5a-4b8c-b129-9d95120db1b5")
        provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
            provisioning_host=provisioning_host,
            registration_id=registration_id,
            id_scope=id_scope,
            x509=x509,
        )
    
        print("Registering provisioning client. Code id = 334527c8-5958-4915-b5f6-e24753d275c4")
        registration_result = await provisioning_device_client.register()
    
        if registration_result.status == "assigned":
            device_client = IoTHubDeviceClient.create_from_x509_certificate(
                x509=x509,
                hostname=registration_result.registration_state.assigned_hub,
                device_id=registration_result.registration_state.device_id,
            )
    
        print("Connecting client to IoT hub. Code id = dace1ead-91dd-4f3e-bbc9-a74d6b08bc1a")
        await device_client.connect()
    
        device_client.on_message_received = message_handler
    
        try:
            print("--Waiting for message--")
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

1. Run the message listener on your Raspberry Pi from Visual Studio Code.

    ```python
    $ ~/repos/IoT $ /bin/python /home/me/repos/IoT/python/raspberrypi/remoteledbar.py
    /home/me/repos/IoT/python/raspberrypi/remoteledbar.py:28: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
      GPIO.setup(LED_channel, GPIO.OUT)
    Ctrl-C to quit'
    Creating x509 cert object from file. Code id = e28c4236-60bb-4d45-adad-2a1b5cd0302e
    Creating provisioning client from certificate. Code id = 53503ead-4f5a-4b8c-b129-9d95120db1b5
    Registering provisioning client. Code id = 334527c8-5958-4915-b5f6-e24753d275c4
    Connecting client to IoT hub. Code id = dace1ead-91dd-4f3e-bbc9-a74d6b08bc1a
    ```

## Send a Remote Command to Turn the LED On or Off

In this section you'll create a program that runs locally to send a command to IoT Hub. Note the command to turn the LED on or off is sent as a custom property and not using the payload.

1. From your windows machine, create a file `c2dsendmsg.py` in your cloned GitHub under the `python\raspberrypi` directory, for example `c:\repos\IoT\python\c2dsendmsg.py`
1. Copy and paste the following import statement

    ```python
    import os
    import time
    from uuid import uuid4
    from azure.iot.hub import IoTHubRegistryManager
    ```

1. Copy and paste the payload data you'll send. Note the payload is JSON for readability.

    ```python
    turnOn = '{ "pause": "0.25", "state": "on", "order": [0,1,2,3,4,5,6,7,8,9] }'
    turnOff = '{ "pause": "0.25", "state": "off", "order": [0,1,2,3,4,5,6,7,8,9] }'
    ```

1. Copy and paste the following main function to send a message to your device from the cloud. Be sure to replace the text `{your device id}` with your device id.

    ```python
    def main():
        deviceId = "{your device id}"
    
        try:
            registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))
            
            # assign system properties
            props={}
            props.update(messageId = "{0}".format(uuid4()))
            props.update(contentType = "application/json")
    
            registry_manager.send_c2d_message(deviceId, turnOn, props)
            time.sleep(2.5)
            registry_manager.send_c2d_message(deviceId, turnOff, props)
        except Exception as ex:
            print ( "Unexpected error {0}" % ex )
    
    if __name__ == "__main__":
        main()
    ```

<!-- Introduction paragraph -->
1. Run the program from Visual Studio Code,

1. Verify your LED turns on when prompted and note the print statement from the code running on your Raspberry Pi.  For example,

    ```azurecli
    --Message Received--
    pin:8, state:off
    pin:12, state:off
    pin:16, state:off
    pin:18, state:off
    pin:22, state:off
    pin:24, state:off
    pin:26, state:off
    pin:32, state:off
    pin:36, state:off
    pin:38, state:off
    --Message Processed--
    ```

## More to Explore

1. Change the message listener and sender code so the LED turns on and off the LEDs using only one message rather than two.
1. Set up the listener as a cron job that starts when your Raspberry Pi starts up or is rebooted.

## Next steps

[Tutorial: Seven Segment Display](tutorial-rasp-segmentdisplay.md)

<!--images-->

[lnk_remoteledbar]: media/tutorial-rasp-remoteledbar/remoteledbar.png
