---
title: Button Switch and Waiting for Edge Lighting of LEDs
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Button Switch and Waiting for Edge Lighting of LEDs

In this tutorial, you learn how to:

- Wire a Button Switch and Two LEDs to your Raspberry Pi
- Code your Button Switch in a simple loop

In the previous tutorial you coded your Raspberry Pi in a continuous loop. In this tutorial you'll 

Following the diagram below, you'll wire a button switch to two LEDs, one red, another green, to show the states of the circuit. Note the various states of the LED's when pressing the button switch:

1. When first starting, the red and green LEDs are both off.
1. When the button switch is pressed, the green LED turns on, while the red remains off.
1. When the button switch is released, the green LED turns off, and the red turns on (until the button switch is pressed again).

    :::image type="content" source="media/tutorial-rasp-switchledsimple/switch2LEDs.gif" alt-text="Button switch with 2 LEDs":::

## Prerequisites

Completed the [Tutorial: Button Switch and Simple Loop Lighting of LEDs](tutorial-rasp-switchledsimple.md)

Supplies:

|Quantity  |Item  |
|:---:|:---|
|1     | Breadboard |
|4     | Male to male jumper wires |
|1     | Button switch |
|1     | Green LED    |
|1     | Red LED    |
|2     | 220Ω Resistors |
|1     | (optional) GPIO Extension Board |
|1     | (optional) 40 pin GPIO cable |

## Wire a Button Switch and Two LEDs to your Raspberry Pi

Below is the circuit we'll construct.

![lnk_ledswitchsimpleschematic]

Following the diagram below:

1. Connect the button switch to the breadboard
1. Connect the red and green LEDs having the cathode (long lead) on a connection terminal and the anode (shorter lead) connected to the breadboard rail.
1. Connect one lead of your 220 resistor to the rail (anode leads from the LEDs), and the other lead to ground.

    :::image type="content" source="media/tutorial-rasp-switchledsimple/simpleswitchled.png" alt-text="Button switch with simple loop":::

## Code your Button Switch

In this section you'll code using the GPIO.input for your button switch with  
`GPIO.wait_for_edge(button, GPIO.RISING, timeout=5000)` . Rather evaluating the `GPIO.input(button)` for a HIGH or LOW signal, the wait_for_edge call blocks the code in your loop from executing until the button switch is pushed (RISING). While the button switch is down, the next line of code, `GPIO.wait_for_edge(button, GPIO.FALLING, timeout=5000)`, blocks the remainder of your loop from executing until the button switch is released.  The timeout is in milliseconds and set for a 5 second timeout. When the code times out, the code execution in your loop continues.

1. [Connect to your Raspberry Pi](https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host) using Visual Studio Code.
1. Create a file `switchledwait.py` in your cloned GitHub under the `python/raspberrypi` directory, for example `~/repos/IoT/python/raspberrypi/switchledwait.py`
1. Import statements and pin assignments.

    ```python
    import RPi.GPIO as GPIO
    import time
    
    # Pin assignments (GPIO.BOARD)
    button = 11 # GPIO17
    led_green = 13 # GPIO27
    led_red = 15 # GPIO22
    ```

1. Copy and Paste the main method.

    ```python
    def main():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led_green, GPIO.OUT)
        GPIO.setup(led_fall, GPIO.OUT)
        GPIO.output(led_green, GPIO.LOW)
        GPIO.output(led_fall, GPIO.LOW)
    
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
        print("Press Ctrl-C to quit'")
        cnt = 0
        result = 0
    
        try:
            while True:
                result = GPIO.wait_for_edge(button, GPIO.RISING, timeout=5000)
                if result is None:
                    print('Timeout waiting for button to be pushed')
                else:
                    GPIO.output(led_green, GPIO.HIGH)
                    GPIO.output(led_fall, GPIO.LOW)
                    print("Button Pushed")
                    result = GPIO.wait_for_edge(button, GPIO.FALLING, timeout=5000)
                    if result is None:
                        print('Timeout waiting for button to be released')
                    else:
                        GPIO.output(led_green, GPIO.LOW)
                        GPIO.output(led_fall, GPIO.HIGH)
                        cnt += 1
                        print("Button Released. Count = {0}".format(cnt))
                time.sleep(0.01) # give the processor time to do other things
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
1. Verify the behavior of the LED lighting.
1. Be sure to gracefully shut down the program by typing ctrl-c.  That way your GPIO ports have been cleaned up and ready for your next project.

## Next steps

[Tutorial: Button Switch and Event Detected Lighting of LEDs](tutorial-rasp-switchledevent.md)

<!--images-->

[lnk_ledswitchsimpleschematic]: media/tutorial-rasp-switchledsimple/ledswitchsimpleschematic.png