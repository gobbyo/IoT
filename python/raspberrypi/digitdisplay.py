import RPi.GPIO as GPIO
import time

#      segment LED
# num   hgfe dcba   hex

# 0 = 	0011 1111   0x3F
# 1 =	0000 0110   0x06
# 2 =	0101 1010   0x5A
# 3 =	0100 1111   0x4F
# 4 =	0110 0110   0x66
# 5 =	0110 1101   0x6D
# 6 =	0111 1101   0x7D
# 7 =	0000 0111   0x07
# 8 =   1111 1111   0xFF
# 9 =   0110 0111   0x67
# A =   1111 0111   0xF7
# b =   1111 1100   0xFC
# C =   1011 1001   0xB9
# d =   0101 1110   0x5E
# F =   1111 0001   0xF1

pins = [4,5,6,12,13,16,17,18]
segnum = [0x3F,0x06,0x5A,0x4F,0x66,0x6D,0x7D,0x07,0xFF,0x67,0xF7,0xFC,0xB9,0x5E,0xF1]

def setup():
    GPIO.setmode(GPIO.BCM)   # Numbers GPIOs by physical location
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def paintnumbers(val):
    i = 0
    for pin in pins:
        GPIO.output(pin,val & (0x01 << i))
        i += 1

def loop():
    while True:
        for val in segnum:
            paintnumbers(val)
            i += 1
            time.sleep(0.25)

def end():
    for pin in pins:
        GPIO.output(pin,0)
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		end()