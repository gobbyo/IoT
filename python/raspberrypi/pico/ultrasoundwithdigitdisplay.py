from machine import Pin
import time
import utime

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

wait = const(200)
digits = [16,19,20,10]
pins = [17,21,12,14,15,18,11,13]
#pins= [a,b,c,d,e,f,g,dot]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
speedofsound = const(343) # meters per second
nano = const(0.00000001)
triggerpin = const(7)
echopin = const(6)

def paintnumber(val, digit):
    digitpin = Pin(digit, Pin.OUT)
    digitpin.low()

    i = 0
    for p in pins:
        pin = Pin(p, Pin.OUT)
        if ((val & (0x01 << i)) >> i) == 1:
            pin.high()
        else:
            pin.low()
        i += 1
    
    time.sleep(.003)

    digitpin.high()

def printfloat(f):
    if f < 100:
        for d in digits:
            pin = Pin(d, Pin.OUT)
            pin.high()
        num = "{:.2f}".format(f)

        for w in range(wait):
            i = len(num)-1
            decimal = False
            d = 3
            while i >= 0 & d >= 0:
                if(num[i].isdigit()):
                    val = segnum[int(num[i])]
                    if decimal:
                        val |= 0x01 << 7
                        decimal = False
                    paintnumber(val, digits[d])
                    d -= 1
                else:
                    decimal = True
                i -= 1

def getdistancemeasure(trig, echo):
    receive = 0
    send = 0

    trig.low()
    utime.sleep_us(2)
    trig.high()
    time.sleep_us(5)
    trig.low()
    
    while echo.value() == 0:
        pass
    send = utime.ticks_us()

    while echo.value() == 1:
        pass
    receive = utime.ticks_us()

    timepassed = receive - send
    return (timepassed * 0.0343) / 2

def main():
    #printfloat(12.75)
    
    trig = Pin(triggerpin, Pin.OUT)
    echo = Pin(echopin, Pin.IN, Pin.PULL_DOWN)

    try:
        while True:
            distance = getdistancemeasure(trig, echo)

            print("{0} centimeters".format(distance))
            printfloat(distance)
        
    finally:
        print("Finished")
        for d in digits:
            pin = Pin(d, Pin.OUT)
            pin.high()

if __name__ == '__main__':
	main()