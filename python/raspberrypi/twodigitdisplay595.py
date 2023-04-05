import RPi.GPIO as GPIO
import time

#   2 digit 7 segmented LED
#
#       digit 1        digit 2        
#        _a_            _a_   
#     f |_g_| b      f |_g_| b
#     e |___| c _h   e |___| c _h
#         d              d       
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

wait = 50
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]

def getArray(val):
    a = [0,0,0,0,0,0,0,0]
    i = 7
    while i >= 0:
        a[i] = (val & (0x01 << i)) >> i
        i -= 1
    return a

def clear2display(latch,clock,data):
    input = [0,0,0,0,0,0,0,0]
    #put latch down to start data sending
    GPIO.output(clock,0)
    GPIO.output(latch,0)
    GPIO.output(clock,1)

    #load data in reverse order
    for i in range(7, -1, -1):
        GPIO.output(clock,0)
        GPIO.output(data, input[i])
        GPIO.output(clock,1)

    #put latch up to store data on register
    GPIO.output(clock,0)
    GPIO.output(latch,1)
    GPIO.output(clock,1)

def painttwodigit(val,digit,latch,clock,data):
    GPIO.output(digit,0)

    #latch down, send data to register
    GPIO.output(clock,0)
    GPIO.output(latch,0)
    GPIO.output(clock,1)
    
    input = getArray(val)

    #load data in register
    for i in range(7, -1, -1):
        GPIO.output(clock,0)
        if input[i] == 1:
            GPIO.output(data,1)
        else:
            GPIO.output(data,0)
        GPIO.output(clock,1)

    #latch up, store data in register
    GPIO.output(clock,0)
    GPIO.output(latch,1)
    GPIO.output(clock,1)

    time.sleep(.004)

    GPIO.output(digit,1)
    clear2display(latch,clock,data)

def printnum(num,digits,latch,clock,data):
    if int(num) < 100:
        for w in range(wait):
            i = len(num)-1
            d = 1
            while i >= 0 & d >= 0:
                if(num[i].isdigit()):
                    val = segnum[int(num[i])]
                    painttwodigit(val,digits[d],latch,clock,data)
                    d -= 1
                i -= 1
    
def main():
    digits = [16,21]
    latch = 38 #RCLK
    clock = 40 #SRCLK
    data = 36 #SER

    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(latch, GPIO.OUT)
        GPIO.setup(clock, GPIO.OUT)
        GPIO.setup(data, GPIO.OUT)
        for d in digits:
            GPIO.setup(d,GPIO.OUT)

        while True:
            i = 0
            while i < 100:
                printnum("{0}".format(i),digits,latch,clock,data)
                i += 1
    finally:
        clear2display(latch,clock,data)
        for d in digits:
            GPIO.output(d,0)

if __name__ == '__main__':
	main()