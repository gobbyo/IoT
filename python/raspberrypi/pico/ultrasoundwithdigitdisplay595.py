from machine import Pin
import time

wait = const(30)
multiplex = .2
millimeters = const(0.001)
ultrasoundlimit = const(4572) #millimeters
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
speedofsound = const(343) # meters per second

triggerpin = const(13)
echopin = const(12)
conversionbuttonpin = const(15)
frontdistancebuttonpin = const(14)

latchpin2digit = const(26) #RCLK
clockpin2digit = const(27) #SRCLK
datapin2digit = const(28) #SER
latchpin4digit = const(7) #RCLK
clockpin4digit = const(6) #SRCLK
datapin4digit = const(8) #SER

class distancestringtools(object):

    def __init__(self):
        self.totalmillimeters = 0
        self.millitoinch = 0.0393701
        self.s_meters = "0"
        self.meters = 0
        self.s_centimeters = "0"
        self.centimeters = 0
        self.s_feet = "0"
        self.feet = 0
        self.s_inches = "0"
        self.inches = 0
    
    def set(self, milli):
        self.totalmillimeters = milli
        s = "{0}".format(milli / 1000)
        n = s.split('.')
        self.s_meters = "{0}".format(n[0])
        self.meters = int(n[0])
        self.centimeters = (milli - (self.meters * 1000)) / 10
        self.s_centimeters = "{0}".format(self.centimeters)

        totalinches = float(milli) * self.millitoinch
        s = "{0}".format(totalinches / 12.0)
        n = s.split('.')
        self.s_feet = "{0}".format(n[0])
        self.feet = int(n[0])
        self.inches = float(totalinches - (float(self.feet) * 12.0))
        self.s_inches = "{0}".format(self.inches)
        
class displaydistance(object):

    def __init__(self):
        self.twodigits =        [16,21]
        self.fourdigits =       [3,2,1,0]
        self.twodata = Pin(datapin2digit, Pin.OUT)
        self.twoclock = Pin(clockpin2digit, Pin.OUT)
        self.twolatch = Pin(latchpin2digit, Pin.OUT)
        self.fourdata = Pin(datapin4digit, Pin.OUT)
        self.fourclock = Pin(clockpin4digit, Pin.OUT)
        self.fourlatch = Pin(latchpin4digit, Pin.OUT)
        
    def __del__(self):
        self.clear2display()
        self.clear4display()
        for d in self.twodigits:
            pin = Pin(d, Pin.OUT)
            pin.low()
        for d in self.fourdigits:
            pin = Pin(d, Pin.OUT)
            pin.low()
    
    def clear2display(self):
        data2d = Pin(datapin2digit, Pin.OUT)
        clock2d = Pin(clockpin2digit, Pin.OUT)
        latch2d = Pin(latchpin2digit, Pin.OUT)    

        clock2d.low()
        latch2d.low()
        clock2d.high()
        
        for i in range(7, -1, -1):
            clock2d.low()
            data2d.low()
            clock2d.high()
        
        clock2d.low()
        latch2d.high()
        clock2d.high()
    
    def clear4display(self):
        data4d = Pin(datapin4digit, Pin.OUT)
        clock4d = Pin(clockpin4digit, Pin.OUT)
        latch4d = Pin(latchpin4digit, Pin.OUT)

        clock4d.low()
        latch4d.low()
        clock4d.high()
        
        for i in range(7, -1, -1):
            clock4d.low()
            data4d.low()
            clock4d.high()

        clock4d.low()
        latch4d.high()
        clock4d.high()

    def getArray(self, val):
        #   [a,b,c,d,e,f,g,h]
        a = [0,0,0,0,0,0,0,0]
        i = 0
        for s in a:
            a[i] = (val & (0x01 << i)) >> i
            i += 1
        print(a)
        return a

    def paintdigit(self, val, digit, data, clock, latch):
        digitpin = Pin(digit, Pin.OUT)
        digitpin.low()

        #latch down, send data to register
        clock.low()
        latch.low()
        clock.high()
        
        input = self.getArray(val)

        #load data in register
        for i in range(7, -1, -1):
            clock.low()
            if input[i] == 1:
                data.high()
            else:
                data.low()
            clock.high()

        #latch up, store data in register
        clock.low()
        latch.high()
        clock.high()

        time.sleep(multiplex)

        digitpin.high()

    def printnumber(self, n):
        num = "{0}".format(n)
        i = len(num)-1
        d = 1

        while i >= 0 & d >= 0:
            val = segnum[int(num[i])]
            print(val)
            self.paintdigit(val,self.twodigits[d],self.twolatch,self.twoclock,self.twodata)
            i -= 1
        d -= 1

    def printfloat(self, f):
        if f < 100:
            for d in self.fourdigits:
                pin = Pin(d, Pin.OUT)
                pin.high()
        
            num = "{:.2f}".format(f)

            i = len(num)-1
            decimal = False
            d = 3
            while i >= 0 & d >= 0:
                if(num[i].isdigit()):
                    val = segnum[int(num[i])]
                    if decimal:
                        val |= 0x01 << 7
                        decimal = False
                    self.paintdigit(val, self.fourdigits[d], self.fourlatch, self.fourclock, self.fourdata)
                    self.clear4display()
                    d -= 1
                else:
                    decimal = True
                i -= 1

def getdistancemeasure():
    trig = Pin(triggerpin,Pin.OUT)
    echo = Pin(echopin,Pin.IN,Pin.PULL_DOWN)

    receive = 0
    send = 0

    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(5)
    trig.low()
    
    while echo.value() == 0:
        pass
    send = time.ticks_us()

    while echo.value() == 1:
        pass
    receive = time.ticks_us()

    timepassed = receive - send

    distanceinmillimeters = round((timepassed * speedofsound * millimeters) / 2)

    if distanceinmillimeters > ultrasoundlimit:
        distanceinmillimeters = 0
    
    trig.low()

    return distanceinmillimeters

def main():   

    frontdistancebutton=Pin(frontdistancebuttonpin,Pin.IN,Pin.PULL_DOWN)
    conversionbutton=Pin(conversionbuttonpin,Pin.IN,Pin.PULL_DOWN)
    display = displaydistance()
    display.clear2display()
    display.clear4display()

    try:
        d = 0
        distance = distancestringtools()

        while True:
            if frontdistancebutton.value():
                d = getdistancemeasure()

            distance.set(d)

            if conversionbutton.value():              
                for w in range(wait):
                    display.printnumber(distance.meters)
                    display.printfloat(distance.centimeters)
            else:
               for w in range(wait):
                    display.printnumber(distance.feet)
                    display.printfloat(distance.inches)

            if frontdistancebutton.value():
                if conversionbutton.value():
                    break
    finally:
        conversionbutton.low()
        frontdistancebutton.low()
        display.__del__()

if __name__ == '__main__':
	main()