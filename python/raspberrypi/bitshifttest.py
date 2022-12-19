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
# A =   1111 0111   0xF7
# b =   1111 1100   0xFC
# C =   1011 1001   0xB9
# d =   1101 1110   0xDE
# E =   1111 0001   0xF1
# F =   1011 1001   0XB9

pins = [4,5,6,12,13,16,17,18]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67,0xF7,0xFC,0xB9,0xDE,0xF1,0XB9]

def paintnumbers(val):
    i = 0
    char = 97
    for pin in pins:
        print("{0}.{1}".format(str(chr(char)),str((val & (0x01 << i)) >> i)))
        i += 1
        char += 1

def main():
    num = 0
    while num < len(segnum):
        if num < 10:
            print("--{0}--".format(num))
        else:
            print("--{0}--".format(chr(65 + (num - 10))))

        paintnumbers(segnum[num])
        num += 1

if __name__ == '__main__':     # Program start from here
		main()