from machine import Pin
import time

wait = const(10)
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
speedofsound = const(343) # centimeters
triggerpin = const(13)
echopin = const(12)
feetbuttonpin = const(15)

class distancestringtools(object):

    def __init__(self):
        self.totalcentimeters = 0
        self.cmtoinch = 0.39370079
        self.meters = "0"
        self.centimeters = "0"
        self.feet = "0"
        self.inches = "0"
    
    def set(self,centimeters):
        self.totalcentimeters = centimeters
        s = "{0}".format(self.totalcentimeters / 100)
        n = s.split('.')
        self.s_meters = "{0}".format(n[0])
        self.meters = int(n[0])
        if self.meters > 0:
            self.centimeters = int(n[1])
        else:
            self.centimeters = centimeters
        self.s_centimeters = "{0}".format(self.centimeters)

        totalinches = self.centimeters * self.cmtoinch
        s = "{0}".format(totalinches / 12.0)
        n = s.split('.')
        self.s_feet = "{0}".format(n[0])
        self.feet = int(n[0])
        if self.feet > 0:
            self.inches = float(totalinches - (float(self.feet) * 12.0))
        else:
            self.inches = totalinches
        self.s_inches = "{0}".format(self.inches)
        
class displaydistance(object):

    def __init__(self):
        self.twodigits = [16,21]
        self.twodigitpins = [26,17,18,20,19,22,28,27]
        #twopinout   = [a, b, c, d, e, f, g, dot]
        self.fourdigits = [6,9,10,5]
        self.fourdigitpins = [7,11,3,1,0,8,4,2]
        #fourpinout   = [a,b,c,d,e,f,g,dot]
        for d in self.fourdigits:
            pin = Pin(d, Pin.OUT)
            pin.high()
        
    def __del__(self):
        for d in self.twodigits:
            pin = Pin(d, Pin.OUT)
            pin.low()
        for d in self.fourdigits:
            pin = Pin(d, Pin.OUT)
            pin.low()
        for n in self.twodigitpins:
            pin = Pin(n, Pin.OUT)
            pin.low()
        for n in self.fourdigitpins:
            pin = Pin(n, Pin.OUT)
            pin.low()

    def paintnumber(self, val, digit, pins):
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
        
        time.sleep(.002)

        digitpin.high()

    def printnumber(self, n):
        for d in self.twodigits:
            pin = Pin(d, Pin.OUT)
            pin.high()

        num = "{0}".format(n)
        i = len(num)-1
        d = 1

        while i >= 0 & d >= 0:
            val = segnum[int(num[i])]
            self.paintnumber(val, self.twodigits[d], self.twodigitpins)
            i -= 1
            d -= 1

    def printfloat(self, f):
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
                    self.paintnumber(val, self.fourdigits[d], self.fourdigitpins)
                    d -= 1
                else:
                    decimal = True
                i -= 1

def getdistancemeasure(trig, echo):
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
    return (timepassed * speedofsound * 0.0001) / 2

def main():   
    trig = Pin(triggerpin, Pin.OUT)
    echo = Pin(echopin, Pin.IN, Pin.PULL_DOWN)
    button=Pin(feetbuttonpin,Pin.IN,Pin.PULL_UP)
    samplemeasurement = False

    try:
        display = displaydistance()

        distancesample = 0
        dist = distancestringtools()
        
        for x in range(1000):
            samplemeasurement = not button.value()

            if(distancesample%15 == 0):
                distance = getdistancemeasure(trig, echo)
                dist.set(distance)

            if samplemeasurement:
                print("Distance ({0} centimeters) in METERS ({1})) & CENTIMETERS ({2})".format(distance,dist.meters,dist.centimeters))
                
                for w in range(wait):
                    display.printnumber(dist.meters)
                    display.printfloat(dist.centimeters)
            else:
                print("Distance ({0} centimeters) in FEET ({1})) & INCHES ({2})".format(distance,dist.feet,dist.inches))

                for w in range(wait):
                    display.printnumber(dist.feet)
                    display.printfloat(dist.inches)
            
            distancesample += 1
        
    finally:
        print("Finished")

if __name__ == '__main__':
	main()