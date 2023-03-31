from machine import Pin
import time

wait = const(20)
multiplex = .02
millimeters = const(0.001)
ultrasoundlimit = const(4572) #millimeters
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
speedofsound = const(343) # meters per second

triggerpin = const(13)
echopin = const(12)
conversionbuttonpin = const(15)
frontdistancebuttonpin = const(14)

fourlatchpin = const(7) #RCLK
fourclockpin = const(6) #SRCLK
fourdatapin = const(8) #SER
twolatchpin = const(26) #RCLK
twoclockpin = const(27) #SRCLK
twodatapin = const(28) #SER

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
        self.twodigit =        [16,21]
        self.fourdigit =       [3,2,1,0]
        self.twodata = Pin(twodatapin, Pin.OUT)
        self.twoclock = Pin(twoclockpin, Pin.OUT)
        self.twolatch = Pin(twolatchpin, Pin.OUT)
        self.fourdata = Pin(fourdatapin, Pin.OUT)
        self.fourclock = Pin(fourclockpin, Pin.OUT)
        self.fourlatch = Pin(fourlatchpin, Pin.OUT)
        
    def __del__(self):
        self.cleardisplay(self.twodata,self.twoclock,self.twolatch)
        self.cleardisplay(self.fourdata,self.fourclock,self.fourlatch)
        for d in self.twodigit:
            pin = Pin(d, Pin.OUT)
            pin.low()
        for d in self.fourdigit:
            pin = Pin(d, Pin.OUT)
            pin.low()

    def getArray(self, val):
        a = [0,0,0,0,0,0,0,0]
        i = 0
        for s in a:
            a[i] = (val & (0x01 << i)) >> i
            i += 1
        return a

    def cleardisplay(self, data, clock, latch):
        clock.low()
        latch.low()
        clock.high()
        
        for i in range(7, -1, -1):
            clock.low()
            data.low()
            clock.high()
        
        clock.low()
        latch.high()
        clock.high()

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

        time.sleep(.003)

        digitpin.high()
        self.cleardisplay(data, clock, latch)

    def printnumber(self, n):
        for d in self.twodigit:
            pin = Pin(d, Pin.OUT)
            pin.high()

        num = "{0}".format(n)
        i = len(num)-1
        d = 1

        while i >= 0:
            val = segnum[int(num[i])]
            self.paintdigit(val,self.twodigit[d],self.twodata,self.twoclock,self.twolatch)
            i -= 1
            d -= 1

    def printfloat(self, f):
        for d in self.fourdigit:
            pin = Pin(d, Pin.OUT)
            pin.high()
        if f < 100: 
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
                    self.paintdigit(val,self.fourdigit[d],self.fourdata,self.fourclock,self.fourlatch)
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