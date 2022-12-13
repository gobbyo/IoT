import time

class LED:
    value = 0

red = LED()
green = LED()
blue = LED()

i = 1
j = 0
k = 0.01
direction = True

while True:
    if j == 0:
        red.value = k
        green.value = 0
        blue.value = 0
        print("i={0} red.value={1}".format(i, red.value))
    elif j == 1:
        red.value = 0
        green.value = k
        blue.value = 0
    else:
        red.value = 0
        green.value = 0
        blue.value = k
        if direction == True:
            i += 1
        else:
            i -= 1

    j += 1
    if j > 2:
        j = 0

    if direction == True:
        if i >= 100:
            direction = False
        else:
            k = float(i/100)
    else:
        if i <= 2:
            direction = True
        else:
            k = float(i/100)

