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

wait = 500
digits = [16,21]
pins = [26,17,18,20,19,22,28,27]
#pins= [a,b,c,d,e,f,g,dot]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]

def painttwodigit(val, digit, twodigitpins):
    digitpin = Pin(digit, Pin.OUT)
    digitpin.low()

    i = 0
    for p in digits:
        pin = Pin(p, Pin.OUT)
        if ((val & (0x01 << i)) >> i) == 1:
            pin.high()
        else:
            pin.low()
        i += 1   
    
    time.sleep(.002)
    
    digitpin.high()

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
        num = '36'

        for w in range(wait):
            i = len(num)-1
            decimal = False
            d = 1
            while i >= 0 & d >= 0:
                if(num[i].isdigit()):
                    val = segnum[int(num[i])]
                    if decimal:
                        val |= 0x01 << 7
                        decimal = False
                    painttwodigit(val,digits[d],pins)
                    d -= 1
                else:
                    decimal = True
                i -= 1
    
def main():
    for d in digits:
        pin = Pin(d, Pin.OUT)
        pin.high()

    try:
        while True:
            printfloat(23.12345)
    finally:
        for d in digits:
            pin = Pin(d, Pin.OUT)
            pin.high()

if __name__ == '__main__':
	main()