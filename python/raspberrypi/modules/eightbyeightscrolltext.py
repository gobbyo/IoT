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
import time

class scrolldisplay(object):

    def __init__(self):
        #default/initialization
        self.LED_rowpins = [9,14,8,12,1,7,2,5]
        self.LED_colpins = [13,3,4,10,6,11,15,16]

    def _createword(self,w):
        word = []
        for l in w:
            word.append(disp.matrix_in_binary(l))
        return word

    #Create a binary buffer for the entire word
    def _createtextbuffer(self, w, size):
        word = self._createword(w)
        buf = []
        row = 0
        while row < size:
            buf.append([])
            for letter in word:
                col = 0
                while col < size:
                    buf[row].append(letter[row][col])
                    col += 1
            row += 1
        return buf

    def _createframebuffer(self, size):
        buf = []
        i = 0
        for i in range(size):
            buf.append([0,0,0,0,0,0,0,0])
        return buf

    def _frame(self, buffer, offset, size):
        display = self._createframebuffer(size)
        col = 0
        while col < size:
            for row in range(size):
                buflen = len(buffer[row])
                if (row < size) and (col + offset < buflen):
                    display[row][col] = buffer[row][col + offset]
                else:
                    exit
            col += 1
        return display

    def scrolltext(self, text, scrollspeed=.125):
        buf = self._createtextbuffer(" {0}".format(text), 8)
        for i in range(len(buf[0])):
            f = self._frame(buf,i,8)
            for row in f:
                print(row)
            print("")
            time.sleep(scrollspeed)