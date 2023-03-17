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

wait = const(400)
digits = [16,19,20,10]
pins = [17,21,12,14,15,18,11,13]
#pins= [a,b,c,d,e,f,g,dot]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
speedofsound = const(343) # meters per second
nano = const(0.00000001)
triggerpin = const(4)
echopin = const(5)

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
    
    time.sleep(.002)

    digitpin.high()

def printfloat(f):
    if f < 100:
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
    
def main():
    # printfloat(12.75)
    for d in digits:
        pin = Pin(d, Pin.OUT)
        pin.high()
    
    trig = Pin(triggerpin, Pin.OUT)
    echo = Pin(echopin, Pin.IN)

    try:
        receive = 0
        send = 0

        while echo.value() == 0:
            trig.high()
            time.sleep(0.000001)
            trig.low()
            send = time.time_ns()

        while echo.value() == 1:
            receive = time.time_ns()

        m_per_sec = speedofsound * ((receive - send) * nano)
        m_per_sec /= 2 # there and back again

        print("{0} centimeters".format(m_per_sec * 10))
        printfloat(m_per_sec * 10)
        
    finally:
        print("Finished")
        for d in digits:
            pin = Pin(d, Pin.OUT)
            pin.high()

if __name__ == '__main__':
	main()