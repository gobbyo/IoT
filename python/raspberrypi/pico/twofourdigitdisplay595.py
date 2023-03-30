from machine import Pin
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

wait = 100
twodigit = [16,21]
fourdigit = [3,2,1,0]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
fourlatchpin = const(7) #RCLK
fourclockpin = const(6) #SRCLK
fourdatapin = const(8) #SER
twolatchpin = const(26) #RCLK
twoclockpin = const(27) #SRCLK
twodatapin = const(28) #SER


def getArray(val):
    a = [0,0,0,0,0,0,0,0]
    i = 0
    for s in a:
        a[i] = (val & (0x01 << i)) >> i
        i += 1
    return a

def cleardisplay(data, clock, latch):
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

def paintdigit(val, digit, data, clock, latch):
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

    time.sleep(.003)

    digitpin.high()
    cleardisplay(data, clock, latch)

def printnumber(n,twolatch,twoclock,twodata):
    num = "{0}".format(n)
    i = len(num)-1
    d = 1

    while i >= 0 & d >= 0:
        val = segnum[int(num[i])]
        paintdigit(val,twodigit[d],twolatch,twoclock,twodata)
        i -= 1
        d -= 1

def printfloat(f,fourdata, fourclock, fourlatch):
    if f < 100: 
        num = "{:.2f}".format(f)

        i = len(num)-1
        decimal = False
        d = 3
        while i >= 0 & d >= 0:
            if(num[i].isdigit()):
                val = segnum[int(num[i])]
                if decimal:
                    val |= 0x01 << 7
                    decimal = False
                paintdigit(val,fourdigit[d],fourdata, fourclock, fourlatch)
                d -= 1
            else:
                decimal = True
            i -= 1
    
def main():
    twodata = Pin(twodatapin, Pin.OUT)
    twoclock = Pin(twoclockpin, Pin.OUT)
    twolatch = Pin(twolatchpin, Pin.OUT)
    fourdata = Pin(fourdatapin, Pin.OUT)
    fourclock = Pin(fourclockpin, Pin.OUT)
    fourlatch = Pin(fourlatchpin, Pin.OUT)

    try:
        for w in range(wait):
            printnumber(23, twodata, twoclock, twolatch)
            printfloat(1.234, fourdata, fourclock, fourlatch)
        for w in range(wait):
            printnumber(11, twodata, twoclock, twolatch)
            printfloat(23.1234, fourdata, fourclock, fourlatch)

    finally:
        cleardisplay(twodata, twoclock, twolatch)
        cleardisplay(fourdata, fourclock, fourlatch)
        for d in fourdigit:
            pin = Pin(d, Pin.OUT)
            pin.high()
        for d in twodigit:
            pin = Pin(d, Pin.OUT)
            pin.high()

if __name__ == '__main__':
	main()