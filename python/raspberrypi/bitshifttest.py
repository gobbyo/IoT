#      segment LED
#
#         a
#        ___
#   f   |   |   b
#       |___|        g
#   e   |   |   c
#       |___|   _    h
#         d
# num   hgfe dcba   hex

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
# A =   0111 0111   0x77
# b =   0111 1100   0x7C
# C =   0011 1001   0x39
# d =   0101 1110   0x5E
# E =   0111 0001   0x71
# F =   0111 1001   0X79

pins = [4,5,6,12,13,16,17,18]
p = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67,0x77,0x7C,0x39,0x5E,0x71,0X79]

def displaynumber(val):
    i = 0
    seg = []
    while i < len(p):
        seg.append(str((val & (0x01 << i)) >> i))
        i += 1
    print(p)
    print(seg)

def main():
    num = 0
    while num < len(segnum):
        if num < 10:
            print("--{0}--".format(num))
        else:
            print("--{0}--".format(chr(65 + (num - 10))))

        displaynumber(segnum[num])
        num += 1

if __name__ == '__main__':     # Program start from here
		main()