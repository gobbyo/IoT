#			C	o	l	u	m	n	s	
#		Pin	13	3	4	10	6	11	15	16
#		9	1	2	3	4	5	6	7	8
#	R	14	9	10	11	12	13	14	15	16
#	o	8	17	18	19	20	21	22	23	24
#	w	12	25	26	27	28	29	30	31	32
#	s	1	33	34	35	36	37	38	39	40
#		7	41	42	43	44	45	46	47	48
#		2	49	50	51	52	53	54	55	56
#		5	57	58	59	60	61	62	63	64

import modules.eightbyeight as disp

LED_rowpins = [9,14,8,12,1,7,2,5]
LED_colpins = [13,3,4,10,6,11,15,16]

def main():
    c = 21
    while c < 128:
        display = disp.matrix_in_binary(chr(c))

        print("+\t\t\t-")
        
        row = 0
        while row < 8:
            col = 0
            while col < 8:
                if display[row][col] == 1:
                    print("{0}\tHIGH\t\t{1}\tLOW".format(LED_rowpins[row], LED_colpins[col]))
                else:
                    print("{0}\tLOW\t\t{1}\tLOW".format(LED_rowpins[row], LED_colpins[col]))
                col += 1
            row += 1
            print("")
        c += 1

if __name__ == "__main__":
    main()