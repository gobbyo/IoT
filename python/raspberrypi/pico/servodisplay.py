from machine import Pin
from servo import sg90
import time

class servoDigitDisplay:
    segpins = [16,17,18,19,20,21,22] # a,b,c,d,e,f,g
    #switchpins = [9,10,11,12,13,14,15]
    latchpin = const(17) #RCLK
    clockpin = const(16) #SRCLK
    datapin = const(24) #SER
    extendAngles = [0,0,0,0,0,0,0]
    retractAngles = [90,90,90,90,90,90,90]
    servospeed = 0.05
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
    segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
    servos = []
    switch = []

    def __init__(self):
        print("servoDigitDisplay constructor")
        for i in self.segpins:
            self.servos.append(sg90(i))

        for i in self.switchpins:
            pin = Pin(i, Pin.OUT)
            pin.off()
            self.switch.append(pin)
        
        latch = Pin(latchpin, Pin.OUT)
        clock = Pin(clockpin, Pin.OUT)
        data = Pin(datapin, Pin.OUT)
    
    def __del__(self):
        for i in range(0,len(self.switch)):
            self.switch[i].off()
        print("servoDigitDisplay destructor")

    def extend(self,index):
        i = self.retractAngles[index]
        self.switch[index].on()
        while i >= self.extendAngles[index]:
            #print("angle = {0}".format(i))
            self.servos[index].move(i)
            time.sleep(self.servospeed)
            i -= 5
        
        #needed when the servo speed is too fast
        self.servos[index].move(self.extendAngles[index])
        time.sleep(.2)
        self.switch[index].off()

    def retract(self,index):
        i = self.extendAngles[index]
        self.switch[index].on()
        while i <= self.retractAngles[index]:
            #print("angle = {0}".format(i))
            self.servos[index].move(i)
            time.sleep(self.servospeed)
            i += 5
        
        #needed when the servo speed is too fast
        self.servos[index].move(self.retractAngles[index])
        time.sleep(.2)
        self.switch[index].off()

    def getArray(self,val):
        a = [0,0,0,0,0,0,0,0]
        i = 0
        for s in a:
            a[i] = (val & (0x01 << i)) >> i
            i += 1
        #print("getArray {0}".format(a))
        return a

    def paintNumber(self,val,show):
        input = []
        input = self.getArray(self.segnum[val])
        if show:
            print("Extend {1}".format(val, input))
        else:
            print("Retract {1}".format(val, input))

        for i in range(0,len(input)):
            if input[i] == 1:
                if show:
                    self.extend(i)               
                else:
                    self.retract(i)