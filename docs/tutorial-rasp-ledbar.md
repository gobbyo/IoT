---
title: Light up an LED 
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Light up an LED bar

<!-- 2. Introductory paragraph 
Required. Lead with a light intro that describes, in customer-friendly language, 
what the customer will learn, or do, or accomplish. Answer the fundamental “why 
would I want to do this?” question. Keep it short.
-->

An LED bar is 10 LEDs in sequence. Once connected properly the LEDs will be controlled by an application that is local on the Raspberry Pi. This project prepares you for the next tutorial to remotely control your LED bar.

<!-- 3. Tutorial outline 
Required. Use the format provided in the list below.
-->

In this tutorial, you learn how to:

- Connect an LED Bar to your Raspberry Pi
- Test the LED bar connection

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- Completed the tutorial to [Configure your Windows Machine](tutorial-configure.md)
- Completed the tutorial to [Connect and configure your Raspberry Pi with Visual Studio Code](tutorial-rasp-connect.md)

## Connect an LED to your Raspberry Pi

In this section you'll wire your Raspberry Pi to light up a Light Emitting Diode (LED) by using the following diagram.

1. From the Raspberry Pi, connect GPIO17 (BCM), PIN 13 (BOARD), to a lead on the 220Ω resistor.  GPIO17 used in this example isn't special, as you can use any GPIO pin, e.g. GPIO2, GPIO12, etc.
1. Connect the positive lead on the LED (the longest lead) to the 220Ω resistor.
1. Connect the negative lead on the LED (the shorter lead) to Ground on the Raspberry Pi

    ![lnk_raspledbar]

    Note the anode (+) pins are located on the same side as the printed identifier.

    ![lnk_raspposledbar]

Supplies:

|#  |Item  |
|:---|:---|
|1     | Breadboard |
|11     | Male to male jumper wires |
|1     | LED Bar Graph |
|10     | 220Ω Resistors |
|1     | (optional) GPIO Extension Board |
|1     | (optional) 40 pin GPIO cable |

## Create Code to Turn Sequentially Switch On or Off the LED Graph
<!-- Introduction paragraph -->
1. [Connect to your Raspberry Pi](https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host) using Visual Studio Code.
1. Create a file `ledbar.py` in your cloned GitHub under the `python/raspberrypi` directory, for example `~/repos/IoT/python/raspberrypi/ledbar.py`
1. Copy and paste the following import statement

    ```python
    import RPi.GPIO as GPIO
    import time
    ```

1. Copy and paste the following method to obtain basic information about your Raspberry Pi. [todo] explain this!

    ```python
    def main():
        LED_pins = [8,12,16,18,22,24,26,32,36,38]
    
        GPIO.setmode(GPIO.BOARD)
    
        for p in LED_pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, GPIO.HIGH)
    
        try:
            on = True
            while True:
                for p in LED_pins:
                    if on:
                        GPIO.output(p, GPIO.LOW)
                    else:
                        GPIO.output(p, GPIO.HIGH)
                    time.sleep(0.25)
                if(on):
                    on = False
                else:
                    on = True
                time.sleep(2)
        except KeyboardInterrupt:
            print("Program shut down")
        finally:
            GPIO.cleanup()
            print("Cleaning up and shutting down")
    
    if __name__ == "__main__":
        main()
    ```

## Run It
<!-- Introduction paragraph -->
1. Start the debugger in Visual Studio Code
1. Verify your LEDs in the bar graph sequentially turn on and off.

## More to Explore

1. Produce different patterns of turning on and off your LED bar display.
1. Reverse the polarity of your LED bar graph:
    - Flip the LED bar graph to have the anode (+) pins connected to the resistors
    - Change the jumper lead from ground to a 3.3v pin
    - Change all occurrences in the code from GPIO.LOW to GPIO.HIGH and GPIO.HIGH to GPIO.LOW

## Next steps

[Tutorial: Remotely Control an LED Bar Graph](tutorial-rasp-remoteled.md)

<!--images-->

[lnk_raspledbar]: media/tutorial-rasp-ledbar/rasp-ledbar.png
[lnk_raspposledbar]: media/tutorial-rasp-ledbar/rasp-posledbar.png
