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

import modules.eightbyeightscrolltext as matrixdisplay
import datetime
import time as time

def main():
    rowpins = [7,11,13,19,21,23,35,37]
    colpins = [8,10,12,16,18,22,24,26]

    stext = matrixdisplay.scrolldisplay()
    stext.rowpins = rowpins
    stext.colpins = colpins

    while True:
        t = datetime.datetime.now()
        buf = t.strftime("Today is %A, %b. %d, %Y")
        stext.scrolltext(buf,2)
        time.sleep(1)
        buf = t.strftime("Time is %I:%M %p")
        stext.scrolltext(buf,2)

if __name__ == "__main__":
    main()