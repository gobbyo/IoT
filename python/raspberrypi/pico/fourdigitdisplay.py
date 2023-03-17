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
# with a dot
# 0 = 	1011 1111   0xBF
# 1 =	1000 0110   0x86
# 2 =	1101 1011   0xDB
# 3 =	1100 1111   0xDF
# 4 =	1110 0110   0xE6
# 5 =	1110 1101   0xED
# 6 =	1111 1101   0xFD
# 7 =	1000 0111   0x87
# 8 =   1111 1111   0xFF
# 9 =   1110 0111   0xE7 


wait = 500
digits = [16,19,20,10]
pins = [17,21,12,14,15,18,11,13]
#pins= [a,b,c,d,e,f,g,dot]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]

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
        num = "{:.2f}".format(f)
        print(num)

        for t in range(300):
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
                    # print("paintnumber(val={0},digits[{1}]={2})".format(val,d,digits[d]))
                    d -= 1
                else:
                    decimal = True
                i -= 1
    
def main():
    for d in digits:
        pin = Pin(d, Pin.OUT)
        pin.high()

    try:
        print("--starting display of digits--")
        printfloat(23.12345)

    except KeyboardInterrupt:
        print("")
        print("Program shut down by user")
    finally:
        print("Program ended")
        for d in digits:
            pin = Pin(d, Pin.OUT)
            pin.high()

if __name__ == '__main__':
	main()