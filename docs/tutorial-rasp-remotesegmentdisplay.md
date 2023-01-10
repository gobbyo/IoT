---
title: Remotely Control a Seven Segment Display
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Remotely Control a Seven Segment Display

In this tutorial, you learn how to:

- Code your Raspberry Pi to Receive Messages to Display 12-hour GMT
- Send Remote Commands to your Seven Segment Display

In the [Tutorial: Remotely Control an LED Display Bar](tutorial-rasp-remoteledbar.md) you remote controlled an LED display bar using the message payload. In this tutorial the call pattern is the same as the display bar, but you'll modify the message payload to describe how to animate the seven segment display. Following the diagram below.

1. You'll use Visual Studio Code to remotely connect to your Raspberry Pi and create listener code to receive messages and change the state of the seven segment display.
1. When you start the code, your Raspberry Pi will use the Device Provisioning Service to create an IoT device client.
1. You'll use the IoT device client to connect to IoT Hub and await for incoming messages.
1. You'll use a local instance of Visual Studio Code to send a message to your Raspberry Pi.
1. The listener program receives the incoming message.
1. The listener program reads the message payload then animates the display of numbers accordingly.

![lnk_remotesegmentdisplay]

## Prerequisites

- [Tutorial: Seven Segment Display](tutorial-rasp-segmentdisplay.md)
- [Tutorial: Remotely Control an LED](tutorial-rasp-remoteled.md)

## Code your Raspberry Pi to Receive Messages to Display 12-hour GMT

1. [Remotely connect to your Raspberry Pi](tutorial-rasp-connect.md#set-up-remote-ssh-with-visual-studio-code).
1. Create a file `remotesegmentdisplay.py` and save it in the `python/rasberrypi` directory from your GitHub forked clone, for example `~/repos/IoT/python/raspberrypi/remotesegmentdisplay.py`. This is a message listener program that runs on your Raspberry Pi.
1. Copy and paste the following import statements into your `remotesegmentdisplay.py` file.

    ```python
    import RPi.GPIO as GPIO
    import time
    import asyncio
    import json
    from decouple import config
    from azure.iot.device import Message, X509
    from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient
    ```

1. Copy and paste the following variables following your import statements from the previous step. Note the `DPS_HOST`, `DPS_SCOPEID`, and `DPS_REGISTRATIONID` should already be added to your [`.env` file](howto-connectionstrings.md) from previous tutorials.

    ```python
    #   7 segmented LED
    #
    #       a
    #     f   b
    #       g
    #     e   c _h
    #       d
    # num   hgfe dcba   hex
    #
    # 0 = 	0011 1111   0x3F
    # 1 =	0000 0110   0x06
    # 2 =	0101 1011   0x5B
    # 3 =	0100 1111   0x4F
    # 4 =	0110 0110   0x66
    # 5 =	0110 1101   0x6D
    # 6 =	0111 1101   0x7D
    # 7 =	0000 0111   0x07
    # 8 =   0111 1111   0x7F
    # 9 =   0110 0111   0x67
    # DP=   1000 0000   0x80
    
    pins = [19,21,8,10,12,29,31,16]
    segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67,0x80]
    provisioning_host = config("DPS_HOST")
    id_scope = config("DPS_SCOPEID")
    registration_id = config("DPS_REGISTRATIONID")
    ```

1. Copy and paste the following function. Note the code reads the message payload data to...

    ```python
    def message_handler(message):
        print("--Message Received--")
        try:
            payload = json.loads(message.data)
            repeat = int(payload['repeat'])
            repeatpause = int(payload['repeatpause'])
            seq = list(payload['time'])

            if payload['pm'] == "True":
                pm = True
            pause = float(payload['pause'])

            for i in range(repeat):
                for s in seq:
                    num = segnum[int(s)]
                    if pm:
                        num |= 0x01 << 7
                        paintnumbers(num)
                        time.sleep(pause)
                        paintnumbers(0x80) #During PM, lights the DP while number changes
                    else:
                        paintnumbers(num)
                        time.sleep(pause)
                        paintnumbers(0) #clear the last digit
                    time.sleep(pause)
                time.sleep(repeatpause)
        finally:
            paintnumbers(0) #clear the DP if PM
            print("--Message Processed--")
    ```

1. Copy and paste code that lights the LEDs for a digit.

    ```python
    def paintnumbers(val):
        i = 0
        for pin in pins:
            GPIO.output(pin,(val & (0x01 << i)) >> i)
            i += 1
    ```

1. Copy and paste the main function. You should be familiar with all the code as presented in previous tutorials.

    ```python
    async def main():
        print("Ctrl-c to quit'")
        GPIO.setmode(GPIO.BOARD)
    
        for p in pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, GPIO.LOW)
    
        print("Creating x509 cert object from file. Code id = 598306d5-bc9c-43e9-867d-4d9939db1e28")
        x509 = X509(
            cert_file=config("X509_CERT_FILE"),
            key_file=config("X509_KEY_FILE"),
            pass_phrase=config("X509_PASS_PHRASE"),
        )
    
        print("Creating provisioning client from certificate. Code id = 459a8019-9176-47e6-a619-6571e3c46baa")
        provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
            provisioning_host=provisioning_host,
            registration_id=registration_id,
            id_scope=id_scope,
            x509=x509,
        )
    
        print("Registering provisioning client. Code id = bedd12a5-338d-44de-89cb-978c621f8eef")
        registration_result = await provisioning_device_client.register()
    
        if registration_result.status == "assigned":
            device_client = IoTHubDeviceClient.create_from_x509_certificate(
                x509=x509,
                hostname=registration_result.registration_state.assigned_hub,
                device_id=registration_result.registration_state.device_id,
            )
    
        print("Connecting client to IoT hub. Code id = c9965aa9-bb8c-4f36-b419-235a60c83c95")
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
    $ ~/repos/IoT $ /bin/python /home/me/repos/IoT/python/raspberrypi/remotesegmentdisplay.py
    /home/me/repos/IoT/python/raspberrypi/remotesegmentdisplay.py:28: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
      GPIO.setup(LED_channel, GPIO.OUT)
    Ctrl-C to quit'
    Creating x509 cert object from file. Code id = 598306d5-bc9c-43e9-867d-4d9939db1e28
    Creating provisioning client from certificate. Code id = 459a8019-9176-47e6-a619-6571e3c46baa
    Registering provisioning client. Code id = bedd12a5-338d-44de-89cb-978c621f8eef
    Connecting client to IoT hub. Code id = c9965aa9-bb8c-4f36-b419-235a60c83c95
    --Waiting for message--
    ```

## Send Remote Commands to your Seven Segment Display

In this section you'll create a program that runs locally to send a command to IoT Hub. Note the command to turn the LED on or off is sent as a custom property and not using the payload.

1. From your windows machine, create a file `c2dsendmsg.py` in your cloned GitHub under the `python\raspberrypi` directory, for example `c:\repos\IoT\python\c2dsendmsg.py`
1. Copy and paste the following import statement

    ```python
    import os
    import time
    import json
    from uuid import uuid4
    from azure.iot.hub import IoTHubRegistryManager
    ```

1. Copy and paste the variables and function that generates the payload. The data you'll send is the current GMT 12-hour time. Since there is only one digit to diplay, time will be split up into 4 numbers played sequentially with a pause between them. For example, 10:03 PM GMT would be expressed having the DP lit to represent "PM", with the 1 pause, 0 pause, 0 pause, 3 pause. The variable "repeattime" is the number of times the entire sequence repeats. For example, a repeattime of 3, means that 1003 would repeat two additional times. The variable "repeatpause" is the amound of time in seconds the display pauses before showing the next sequence of digits. The variable "pause" is the wait time between digits.

    ```python
    repeattime = 3
    repeatpause = 1
    pause = 0.5

    # Sample JSON for 12-hour GMT at 10:35 AM
    # { "repeat": 5, "repeatpause": 1, "pause": 0.5, "pm": "False", "time": [1,0,3,5]}
    def getpayload():
        j = {}
        j.update(repeat = repeattime)
        j.update(repeatpause = repeatpause)
        j.update(pause = pause)
    
        t = []
        hour = time.gmtime().tm_hour
        
        if hour > 12:
            j.update(pm = 'True')
            hour -= 12
        else:
            j.update(pm = 'False')
    
        h = str(hour).zfill(2)
        m = str(time.gmtime().tm_min).zfill(2)
        t.append(int(h[0]))
        t.append(int(h[1]))        
        t.append(int(m[0]))
        t.append(int(m[1]))
        j.update(time = t)
        return json.dumps(j)
    ```

1. Copy and paste the following main function to send a message to your device from the cloud. Be sure to replace the text `{your device id}` with your device id.

    ```python
    def main():
        deviceId = "raspberrypi2"
    
        try:
            registry_manager = IoTHubRegistryManager(os.getenv("IOTHUB_CONNECTION_STRING"))
            
            # assign system properties
            props={}
            props.update(messageId = "{0}".format(uuid4()))
            props.update(contentType = "application/json")
    
            registry_manager.send_c2d_message(deviceId, getpayload(), props)
        except Exception as ex:
            print ( "Unexpected error {0}" % ex )
    
    if __name__ == "__main__":
        main()
    ```

<!-- Introduction paragraph -->
1. Run the program from Visual Studio Code,

1. Verify your seven segment display is showing the GMT.  For example,

    ```azurecli
    --Message Received--
    --Message Processed--
    ```

## More to Explore

- Display the number of bells on a mariners clock, where each number represents a 1/2 hour until you get to 12, then the rotation starts over.
- Display the outside temperature and humidity.

## Next steps

<!--images-->

[lnk_remotesegmentdisplay]: media/tutorial-rasp-remotesegmentdisplay/remotesegmentdisplay.png
