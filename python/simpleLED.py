from gpiozero import LED
import time

red = LED(12)
green = LED(6)
blue= LED(10)

i = 0
j = 0

while True:
    if j == 0:
        red.on()
        green.off()
        blue.off()
    elif j == 1:
        red.off()
        green.on()
        blue.off()
    else:
        red.off()
        green.off()
        blue.on()
    time.sleep(0.25)
    i += 1
    j += 1
    if j > 2:
        j = 0

red.off()
green.off()
blue.off()