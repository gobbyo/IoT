import RPi.GPIO as GPIO
import modules.eightbyeight as disp
import time

class scrolldisplay(object):

    def __init__(self):
        #default/initialization
        self.rowpins = [7,11,13,19,21,23,35,37]
        self.colpins = [8,10,12,16,18,22,24,26]
        self.wait_time = 0.002
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        for rowpin in self.rowpins:
            GPIO.setup(rowpin, GPIO.OUT)
            GPIO.output(rowpin, GPIO.LOW)
        
        for colpin in self.colpins:
            GPIO.setup(colpin, GPIO.OUT)
            GPIO.output(colpin, GPIO.LOW)
    
    def __del__(self):
        GPIO.cleanup()
    
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

    def _paintscreen(self, buffer, scrollspeed):
        s = scrollspeed
        while s > 0:
            for colpin in self.colpins:
                GPIO.output(colpin, GPIO.HIGH)
            row = 0
            for val in buffer:
                GPIO.output(self.rowpins[row],GPIO.HIGH)
                i = 0
                for colpin in self.colpins:
                    if val[i] > 0:
                        GPIO.output(colpin,GPIO.LOW)
                    i += 1
                time.sleep(self.wait_time)
                
                for colpin in self.colpins:
                    GPIO.output(colpin, GPIO.HIGH)
                GPIO.output(self.rowpins[row],GPIO.LOW)
                row += 1
            s -= 1

    def scrolltext(self, text, scrollspeed=5):
        buf = self._createtextbuffer(" {0}".format(text), 8)
        for i in range(len(buf[0])):
            f = self._frame(buf,i,8)
            self._paintscreen(f,scrollspeed)