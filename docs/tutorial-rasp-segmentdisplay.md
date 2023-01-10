---
title: Seven Segment Display 
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Seven Segment Display

In this tutorial, you learn how to:

- Wire a single digit seven-segment display
- Test the segment display connection

A Seven Segment display is a type of electronic device that is used to display decimal numerals and some alphabetical characters. It consists of seven segments, each of which is a LED or LCD display element, arranged in a particular pattern to form the digits and some letters. The segments are labeled with the letters "a" through "g" as shown in the diagram below:

![lnk_segdisplay]

A one-digit Seven Segment display can display any one decimal digit from 0 to 9. It is commonly used in digital clocks, calculators, and other electronic devices where numerical information is displayed. It can also be used to display some alphabetical characters, such as "E" and "H".

One-digit Seven Segment displays are inexpensive, easy to use, and have a relatively low power consumption compared to other types of displays. They are also available in different sizes and colors, making them suitable for a wide range of applications.

For this tutorial, your seven-segment display will be controlled by an application that is local on the Raspberry Pi.

## Prerequisites

Completed the [Tutorial: Light up an LED bar](tutorial-rasp-ledbar.md)

Supplies:

|Quantity  |Item  |
|:---:|:---|
|1     | Breadboard |
|9     | Male to male jumper wires |
|1     | Seven Segment Display |
|8     | 220Ω Resistors |
|1     | (optional) GPIO Extension Board |
|1     | (optional) 40 pin GPIO cable |

## Wire your seven-segment display to your Raspberry Pi

In this section you'll wire your Raspberry Pi to display numbers on a seven-segment display. Below is the circuit we'll construct.

![lnk_schematic_segmentdisplay]

There are 10 pins on the single digit seven-segment display.  The pins correspond to the function from the previous picture. For example, the Raspberry Pi pin 7 controls the "a" LED on the segment display.

Complete the wiring of your seven segment display by using the following diagram.

1. Connect your seven segment display to the breadboard.
1. Connect a lead of the 220Ω resistor to the breadboard rail strip, and the other lead to your Raspberry Pi ground (GND) GPIO pin.
1. Connect a jumper wire from your seven segment display ground pins (3 & 8) to the rail strip connected to your 220Ω resistor.
1. Connect one end of the jumper wire to a terminal strip that corresponds to each Raspberry GPIO Pin: 19,21,8,10,12,29,31,and 16.
1. For each jumper wire, connect each GPIO pin to each pin on your segment display per the wiring diagram.

![lnk_segdisplaywiring]

## Create Test Code to Show Digits

You can use binary to control each LED in the display `a-h` because each LED in a seven-segment display has a binary state: on (1) or off (0).  Note that `h` represents the dot point (dp). For example, the number five is displayed with LEDs `a`, `c`, `d`, `f`, and `g` turned on, and `b`, and `e` are off.

![lnk_displayfive]

In code you'll represent the LED state for each segment as a = 1 (on), b = 0 (off), c = 1 (on), and so on. The entire conversion for the display of number five is as follows,

```python
# num   hgfe dcba   hex
# 5 =	0110 1101   0x6D
```

⚠️ Note the conversion above is NOT the binary or hex representation of the number 5, which would be 0000 0101 (binary) and 0x05 (hex).

The entire list of numbers an A-F is as follows:

```python
# num   hgfe dcba   hex

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
# A =   0111 0111   0x77
# b =   0111 1100   0x7C
# C =   0011 1001   0x39
# d =   0101 1110   0x5E
# E =   0111 0001   0x71
# F =   0111 1001   0X79
```

You'll need to use bit masking to determine each `a-h` LED to turn on or off as you loop through the 8 binary digits. Bit masking uses the `&` operator to determine the outcome of two binary values, for example 1 & 1 = 1 whereas 1 & 0 = 0. To determine if LED `a` for the number "5" (`0110 1101`) is turned on or off, you'll bit mask the `a` register using '0000 0001' (0x01) as follows,

```python
# hgfe dcba
# 0110 1101
#     &
# 0000 0001
# ---- ----
# 0000 0001 ('a' LED is set to on)
```

To determine the value of the 'b' LED for the number "5" (`0110 1101`), you'll shift `0x01` left (`<<`) to the 'b' register as ('0x01 << 1') to bitmask the 'b' register (`0000 0010`). For example,

```python
# hgfe dcba
# 0110 1101
#     &
# 0000 0010
# ---- ----
# 0000 0000 ('b' LED should be set to off)
```

Try the following test code to experiment with bitmasking digits for your Seven Segment display.

1. Create a file `bitshifttest.py` in your forked GitHub under the `python/raspberrypi` directory, for example `~/repos/IoT/python/raspberrypi/bitshifttest.py`
1. Copy and paste the following variables.

    ```python
    p = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']
    segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67,0x77,0x7C,0x39,0x5E,0x71,0X79]
    ```

1. Copy and paste the following method to calculate which LED to turn on or off.

    ```python
    def displaynumber(val):
        i = 0
        seg = []
        while i < len(p):
            seg.append(str((val & (0x01 << i)) >> i))
            i += 1
        print(p)
        print(seg)
    ```

1. Copy and paste the main function to iterate through all the possible display values.

    ```python
    def main():
        num = 0
        while num < len(segnum):
            if num < 10:
                print("--{0}--".format(num))
            else:
                print("--{0}--".format(chr(65 + (num - 10))))
    
            displaynumber(segnum[num])
            num += 1
    
    if __name__ == '__main__':     # Program start from here
    		main()
    ```

1. Run the program in the VS code debugger.  Your output will display the 1 (on) or 0 (off) value for each LED segment a-f as follows,

    ```python
    --0--
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ['1', '1', '1', '1', '1', '1', '0', '0']
    --1--
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ['0', '1', '1', '0', '0', '0', '0', '0']
    --2--
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ['1', '1', '0', '1', '1', '0', '1', '0']
    ```

## Code your Seven Segment Display

In this section you'll create code that will iterate through all the numbers and show them on your seven-segment display.

<!-- Introduction paragraph -->
1. [Connect to your Raspberry Pi](https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host) using Visual Studio Code.
1. Create a file `segmentdisplay.py` in your cloned GitHub under the `python/raspberrypi` directory, for example `~/repos/IoT/python/raspberrypi/segmentdisplay.py`
1. Copy and paste the following import statement

    ```python
    import RPi.GPIO as GPIO
    import time
    ```

1. Copy and paste the method below having logic you bit shift tested to display a single digit.

    ```python
    def paintnumbers(val):
        i = 0
        for pin in pins:
            GPIO.output(pin,(val & (0x01 << i)) >> i)
            i += 1
    ```

1. Copy and paste the following method to sequentially show numbers 0 through 9 in your seven segment display.

    ```python
    def main():
        GPIO.setmode(GPIO.BOARD)   # Pins
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
    
        try:
            print("--starting display of digits--")
            while True:
                for val in segnum:
                    paintnumbers(val)
                    time.sleep(0.5)
        except KeyboardInterrupt:
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
1. Verify numbers appear in your Seven Segment display.

## More to Explore

1. Extend the functionality to light the `dp`. For example, have the `dp` light up for the characters A through F.
1. Extend the numbers to include letters like `H`, `h`, or symbols like `-`.

## Next steps

[Tutorial: Remotely Control a Seven Segment Display](tutorial-rasp-remoteled.md)

<!--images-->

[lnk_segdisplay]: media/tutorial-rasp-digitsegment/segdisplay.png
[lnk_schematic_segmentdisplay]: media/tutorial-rasp-digitsegment/schematicsegmentdisplay.png
[lnk_segdisplaywiring]: media/tutorial-rasp-digitsegment/segdisplaywiring.png
[lnk_displayfive]: media/tutorial-rasp-digitsegment/displayfive.png
[lnk_displayconversion]: media/tutorial-rasp-digitsegment/displayconversion.png