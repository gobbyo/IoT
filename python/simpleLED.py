from gpiozero import PWMLED
import time

red = PWMLED(12)
green = PWMLED(6)
blue= PWMLED(10)

luminIncr = 0.05
i = 0
j = 0
k = 0.0
direction = True

while True:
    if j == 0:
        red.value = k
        green.off()
        blue.off()
    elif j == 1:
        red.off()
        green.value = k
        blue.off()
    else:
        red.off()
        green.off()
        blue.value = k
    time.sleep(0.25)
    i += 1
    j += 1
    if j > 2:
        j = 0

    if direction == True:
        k += luminIncr
        if k >= 1.0:
            direction == False
    else:
        k -= luminIncr
        if k <= 0:
            direction == True
red.off()
green.off()
blue.off()