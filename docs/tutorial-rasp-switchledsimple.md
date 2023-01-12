---
title: Button Switch and Simple Loop Lighting of LEDs  
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Button Switch and Simple Loop Lighting of LEDs

In this tutorial, you learn how to:

- [todo]

A button switch is a type of electrical switch that is activated by pressing a button. They are commonly used in electronic devices to turn them on or off, or to perform other functions such as adjusting the volume or changing the channel. The benefits of button switches include their ease of use and the ability to control electronic devices with a simple press of a button. Additionally, button switches are relatively inexpensive and widely available, making them a popular choice for use in a wide range of electronic devices.

Following the diagram below, you'll wire a button switch to two LEDs, one red, another green, to show the states of the circuit. Note the various states of the LED's when pressing the button switch:

1. When first starting, the red and green LEDs are off
1. When the button switch is pressed, the green LED turns on, while the red remains off
1. When the button switch is released, the green LED turns off, and the red turns on (until the button switch is pressed again)

    :::image type="content" source="media/tutorial-rasp-switchledsimple/switch2LEDs.gif" alt-text="Button switch with 2 LEDs":::

## Prerequisites

Completed the...

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

1. Import statements and variables.

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
        GPIO.setup(led_red, GPIO.OUT)
        GPIO.output(led_green, GPIO.LOW)
        GPIO.output(led_red, GPIO.LOW)
    
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
        print("Press Ctrl-C to quit'")
        last = 0
        cur = 0
        cnt = 0
    
        try:
            while True:
                cur = GPIO.input(button)
                if cur != last:
                    if GPIO.input(button) == GPIO.LOW:
                        GPIO.output(led_green, GPIO.LOW)
                        GPIO.output(led_red, GPIO.HIGH)
                        cnt += 1
                        print("Button Released. Count = {0}".format(cnt))
                    else:
    
                        GPIO.output(led_green, GPIO.HIGH)
                        GPIO.output(led_red, GPIO.LOW)
                        print("Button Pushed")
                    last = cur
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

## Next steps

<!--images-->

[lnk_ledswitchsimpleschematic]: media/tutorial-rasp-switchledsimple/ledswitchsimpleschematic.png