import RPi.GPIO as GPIO
import time

a = 4 # 0
b = 5 # 1
c = 6 # 2
d = 12 # 3
e = 13 # 4
f = 16 # 5
g = 17 # 6
z = 18 # 7

numbers = [[i * j for j in range(8)] for i in range(10)]
for i in range(10):
    for j in range(8):
        numbers[i][j] = 0

def setup():
    GPIO.setmode(GPIO.BCM)   # Numbers GPIOs by physical location
    GPIO.setup(a, GPIO.OUT)
    GPIO.setup(b, GPIO.OUT)
    GPIO.setup(c, GPIO.OUT)
    GPIO.setup(d, GPIO.OUT)
    GPIO.setup(e, GPIO.OUT)
    GPIO.setup(f, GPIO.OUT)
    GPIO.setup(g, GPIO.OUT)
    GPIO.setup(z, GPIO.OUT)

    i = 0
    zero = numbers[0]
    while i < 6:
        zero[i] = 1
        i += 1
    
    numbers[1][1] = 1
    numbers[1][2] = 1

    numbers[2][0] = 1
    numbers[2][1] = 1
    numbers[2][3] = 1
    numbers[2][4] = 1
    numbers[2][6] = 1

    numbers[3][0] = 1
    numbers[3][1] = 1
    numbers[3][2] = 1
    numbers[3][3] = 1
    numbers[3][6] = 1

    numbers[4][1] = 1
    numbers[4][2] = 1
    numbers[4][5] = 1
    numbers[4][6] = 1

    numbers[5][0] = 1
    numbers[5][2] = 1
    numbers[5][3] = 1
    numbers[5][5] = 1
    numbers[5][6] = 1

    numbers[6][2] = 1
    numbers[6][3] = 1
    numbers[6][4] = 1
    numbers[6][5] = 1
    numbers[6][6] = 1

    numbers[7][0] = 1
    numbers[7][1] = 1
    numbers[7][2] = 1

    i = 0
    while i < 7:
        numbers[8][i] = 1
        i += 1

    numbers[9][0] = 1
    numbers[9][1] = 1
    numbers[9][2] = 1
    numbers[9][5] = 1
    numbers[9][6] = 1

def paintnumbers(i):
    GPIO.output(a,numbers[i][0])
    GPIO.output(b,numbers[i][1])
    GPIO.output(c,numbers[i][2])
    GPIO.output(d,numbers[i][3])
    GPIO.output(e,numbers[i][4])
    GPIO.output(f,numbers[i][5])
    GPIO.output(g,numbers[i][6])

def loop():
    while True:
        i = 0
        while i < 10:
            paintnumbers(i)
            i += 1
            time.sleep(0.25)
        i = 9
        while i >= 0:
            paintnumbers(i)
            time.sleep(0.5)
            i -= 1

def end():
    GPIO.output(a,0)
    GPIO.output(b,0)
    GPIO.output(c,0)
    GPIO.output(d,0)
    GPIO.output(e,0)
    GPIO.output(f,0)
    GPIO.output(g,0)
    GPIO.output(z,0)
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		end()