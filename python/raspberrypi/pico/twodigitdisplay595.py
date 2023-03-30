from machine import Pin
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
digits = [16,21]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
latchpin = const(26) #RCLK
clockpin = const(27) #SRCLK
datapin = const(28) #SER

def getArray(val):
    a = [0,0,0,0,0,0,0,0]
    i = 7
    while i >= 0:
        a[i] = (val & (0x01 << i)) >> i
        i -= 1
    return a

def clear2display():
    data = Pin(datapin, Pin.OUT)
    clock = Pin(clockpin, Pin.OUT)
    latch = Pin(latchpin, Pin.OUT)

    clock.low()
    latch.low()
    clock.high()
    
    for i in range(7, -1, -1):
        clock.low()
        data.low()
        clock.high()
    
    clock.low()
    latch.high()
    clock.high()

def painttwodigit(val, digit):
    data = Pin(datapin, Pin.OUT)
    clock = Pin(clockpin, Pin.OUT)
    latch = Pin(latchpin, Pin.OUT)

    digitpin = Pin(digit, Pin.OUT)
    digitpin.low()

    #latch down, send data to register
    clock.low()
    latch.low()
    clock.high()
    
    input = getArray(val)

    #load data in register
    for i in range(7, -1, -1):
        clock.low()
        if input[i] == 1:
            data.high()
        else:
            data.low()
        clock.high()

    #latch up, store data in register
    clock.low()
    latch.high()
    clock.high()

    time.sleep(.004)

    digitpin.high()
    clear2display()

def printnum(num):
    if int(num) < 100:
        for w in range(wait):
            i = len(num)-1
            d = 1
            while i >= 0 & d >= 0:
                if(num[i].isdigit()):
                    val = segnum[int(num[i])]
                    painttwodigit(val,digits[d])
                    d -= 1
                i -= 1
    
def main():
    try:
        while True:
            i = 0
            while i < 100:
                printnum("{0}".format(i))
                i += 1
    finally:
        clear2display()
        for d in digits:
            pin = Pin(d, Pin.OUT)
            pin.high()

if __name__ == '__main__':
	main()