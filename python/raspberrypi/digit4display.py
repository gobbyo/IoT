import RPi.GPIO as GPIO
import time

#   7 segmented LED
#
#        _a_
#     f |_g_| b
#     e |___| c _h
#         d
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

def paintnumber(val, digit):
    GPIO.output(digit, GPIO.LOW)
    i = 0
    for pin in pins:
        GPIO.output(pin,(val & (0x01 << i)) >> i)
        i += 1
    time.sleep(.0025)
    GPIO.output(digit, GPIO.HIGH)

def displaytime():
    t = time.localtime()
    return("{:02d}{:02d}".format(t.tm_hour,t.tm_min))

def main():
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
            # num = input("0-9999: ")
            num = displaytime()
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