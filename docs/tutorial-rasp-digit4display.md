---
title: Four Digit Seven Segment Display 
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Four Digit Seven Segment Display

In this tutorial, you learn how to:

- Wire a four digit, seven-segment display
- Test the four digit display connection

A four digit, seven segment display is a type of electronic display device that is used to show numerical information. It consists of four individual segments, each of which can display a single digit (0-9). Each segment is made up of seven individual LED lights arranged in the shape of the numeral 8, which allows for the display of all ten digits (0-9) as well as some letters. These displays are commonly found in digital clocks, timers, and other electronic devices that require the display of numerical information. They are also used in industrial and automotive applications.

A four digit, seven segment display has several benefits:

- *Low cost*. Seven segment displays are relatively inexpensive to manufacture, making them a cost-effective option for many applications.
- *High visibility*. The segments are made from LEDs, which are highly visible, even in bright sunlight or low light conditions.
- *Easy to read*. The segmented design makes the numbers and letters easy to read, even from a distance.
- *Versatile*. The ability to display numbers and some letters makes it a versatile choice for many different applications.
- *Low power consumption*. Seven segment displays are relatively low power, which makes them an ideal choice for battery-operated or portable devices.
- *Durable*. Seven segment displays are built to last and have a long life span, providing a reliable display solution.
- They can be *easily controlled by microcontroller* and other digital devices, making the integration easy and simple.
- They can be *used in harsh environments* as they are available in different enclosures such as plastic, metal, and glass.

For this tutorial, your four digit, seven-segment display will be controlled by an application that is local on the Raspberry Pi.

## Prerequisites

[Tutorial: Seven Segment Display](tutorial-rasp-segmentdisplay.md)

Supplies:

|Quantity  |Item  |
|:---:|:---|
|1     | Breadboard |
|16     | Male to male jumper wires |
|1     | Four Digit Seven Segment Display |
|4     | 220Ω Resistors |
|1     | (optional) GPIO Extension Board |
|1     | (optional) 40 pin GPIO cable |

## Wire your four digit segment display to your Raspberry Pi

In this section you'll wire your Raspberry Pi to display numbers on a four digit segment display. Below is the circuit you'll construct.

![lnk_digit4schematic]

There are 12 pins for the display. Pins labelled D1, D2, D3, and D4 are the pins to switch the digit on (GPIO.LOW) or off (GPIO.HIGH). For example, pin 7 controls the leftmost digit. The remaining pins control each segment of the display "a" through "g". Note that "h" is the dot point (dp).

Like the previous seven segment display tutorial, setting the 8th pin "a" on the four digit display will cause the "a" LED to light up on all four digits. You'll have to turn on the digit to paint the number on the display while the remaining digits are off. For example, to display the number 6890, you'll write code that turns off digits 2, 3, and 4, paints the number "6" onto digit one then turn off digit 1 while digit 2 paints the number "9" and so on.

Complete the wiring of your four digit segment display by using the following diagram.

1. Connect your four digit segment display to your breadboard as diagrammed below. Note the lettering on the component is the bottom where pin 1-6 reside.
1. With 4 male jumpers, connect one end to the four display digit pins 6, 7, 10 and 11.
1. 

![lnk_digit4wiring]

## Code your Seven Segment Display

In this section you'll create code that will iterate through all the numbers and show them on your seven-segment display.

<!-- Introduction paragraph -->
1. [Connect to your Raspberry Pi](https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host) using Visual Studio Code.
1. Create a file `digit4display.py` in your cloned GitHub under the `python/raspberrypi` directory, for example `~/repos/IoT/python/raspberrypi/digit4display.py`
1. Copy and paste the following import statements and variables.

    ```python
    import RPi.GPIO as GPIO
    import time
    
    #   4 digit 7 segmented LED
    #
    #       digit 1        digit 2        digit 3        digit 4
    #        _a_            _a_            _a_            _a_
    #     f |_g_| b      f |_g_| b      f |_g_| b      f |_g_| b
    #     e |___| c _h   e |___| c _h   e |___| c _h   e |___| c _h
    #         d              d              d              d
    #
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
    
    wait = 1000
    digits = [32,36,38,40]
    pins = [19,21,8,10,12,29,31,16]
    segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
    ```

1. Copy and paste the method below to paint the number on a single digit from the four possible digits. The sleep time of 0.0025 of a second is the time to make the digits appear that a multi-digit number steadily shows without flashing. You can try a larger sleep time to see how the digits are individually painted.

    ```python
    def paintnumber(val, digit):
        GPIO.output(digit, GPIO.LOW)
        i = 0
        for pin in pins:
            GPIO.output(pin,(val & (0x01 << i)) >> i)
            i += 1
        time.sleep(.0025)
        GPIO.output(digit, GPIO.HIGH)
    ```

1. Copy and paste this method for the option to display a 24 hour clock.

    ```python
    def displaytime():
        t = time.localtime()
        return("{:02d}{:02d}".format(t.tm_hour,t.tm_min))
    ```

1. Copy and paste the main method.

    ```python
    def main():
        time.sleep(20) #need to wait 20 seconds for cronjobs
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)   # Pins
    
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
        
        for d in digits:
            GPIO.setup(d, GPIO.OUT)
            GPIO.output(d, GPIO.HIGH)
    
        try:
            print("--starting display of digits--")
            while True:
                num = input("0-9999: ")
                # num = displaytime()
                iter = int(wait/len(num))
                for w in range(iter):
                    i = len(num)-1
                    while i >= 0:
                        paintnumber(segnum[int(num[i])], digits[i])
                        i -= 1
    
        except KeyboardInterrupt:
            print("")
            print("Program shut down by user")
        finally:
            for pin in pins:
                GPIO.output(pin,0)
            GPIO.cleanup()
    
    if __name__ == '__main__':
    	main()
    ```

## Run It
<!-- Introduction paragraph -->
1. Start the debugger in Visual Studio Code
1. Type a number in the console app to display `num = input("0-9999: ")`.  
1. Verify numbers appear in your four digit segment display.
1. Next, uncomment the line `# num = displaytime()` and comment out the `num = input("0-9999: ")`.
1. Verify a 24 hour clock time is displaying in your four digit segment display.

## More to Explore


## Next steps

[Tutorial: Remotely Control a Seven Segment Display](tutorial-rasp-remotesegmentdisplay.md)

<!--images-->

[lnk_digit4schematic]: media/tutorial-rasp-digit4display/digit4schematic.png
[lnk_digit4wiring]: media/tutorial-rasp-digit4display/digit4wiring.png