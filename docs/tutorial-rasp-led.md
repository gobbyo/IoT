---
title: Light up an LED 
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Light up an LED

In this tutorial, you learn how to:

- Connect an LED to your Raspberry Pi
- Test the LED connection

Lighting an LED is the starting point for electronic projects. Once connected properly the LED will be controlled by an application that is local on the Raspberry Pi. This project prepares you for the next tutorial to remotely control your LED.

## Prerequisites

- Completed the [Tutorial: Send Hostname and IP address to the Cloud](tutorial-rasp-d2cipandhostname.md)

## Connect an LED to your Raspberry Pi

In this section you'll wire your Raspberry Pi to light up a Light Emitting Diode (LED) by using the following diagram.

1. From the Raspberry Pi, connect GPIO17 (BCM), PIN 13 (BOARD), to a lead on the 220Ω resistor.  GPIO17 used in this example isn't special, as you can use any GPIO pin, e.g. GPIO2, GPIO12, etc.
1. Connect the positive lead on the LED (the longest lead) to the 220Ω resistor.
1. Connect the negative lead on the LED (the shorter lead) to Ground on the Raspberry Pi

    ![lnk_raspled]

Supplies:

|#  |Item  |
|:---|:---|
|1     | [Breadboard](https://www.circuitbread.com/ee-faq/what-is-a-breadboard) |
|2     | [Male to male jumper wires](https://store.robotechvalley.com/product/male-to-male-jumper-wires/#:~:text=Description%3A%20male%20to%20male%20jumper%20wires%20These%20superior,arrangement%20of%20every%20one%20of%20ten%20rainbow%20tone.) |
|1     | LED |
|1     | 220Ω Resistor |
|1     | (optional) GPIO Extension Board |
|1     | (optional) 40 pin GPIO cable |

## Create Code to Turn the LED on and off
<!-- Introduction paragraph -->
1. [Connect to your Raspberry Pi](https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host) using Visual Studio Code.
1. Create a file `led.py` in your cloned GitHub under the `python/raspberrypi` directory, for example `~/repos/various/python/raspberrypi/led.py`
1. Copy and paste the following import statement

    ```python
    import RPi.GPIO as GPIO
    ```

1. Copy and paste the following method to obtain basic information about your Raspberry Pi. [todo] explain this!

    ```python
    def main():
        LED_channel = 17
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_channel, GPIO.OUT)
        GPIO.output(LED_channel, GPIO.LOW)
    
        print("Press Ctrl-C to quit'")
    
        try:
            while True:
                s = input("Type 'On' or 'Off': ")
                if s == 'On':
                    GPIO.output(LED_channel, GPIO.HIGH)
                    print("On")
                else:
                    GPIO.output(LED_channel, GPIO.LOW)
                    print("Off")
                print("-----")
        except KeyboardInterrupt:
            print("Program shut down by user")
        finally:
            GPIO.cleanup()
            print("Cleaning up and shutting down")
    
    if __name__ == "__main__":
        main()
    ```

## Run It
<!-- Introduction paragraph -->
1. Start the debugger in Visual Studio Code
1. Type 'On' or 'Off' when prompted in the `DEBUG CONSOLE`
1. Verify your LED turns on and off when prompted

## More to Explore

1. Have your LED flash to represent the time in hours and minutes in military time. For example, 2:30 would be 2 flashes, a few second pause, then 3 flashes (one flash for every 10 minute)
1. Add multiple LEDs like Green, Yellow, and Red.

## Next steps

[Tutorial: Remotely Control an LED](tutorial-rasp-remoteled.md)

<!--images-->

[lnk_raspled]: media/tutorial-rasp-led/rasp-led.png
