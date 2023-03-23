from machine import Pin
import time

wait = const(10)
twodigits = [16,21]
twodigitpins = [26,17,18,20,19,22,28,27]
fourdigits = [6,9,10,5]
fourdigitpins = [7,11,3,1,0,8,4,2]
#fourdigitpins= [a,b,c,d,e,f,g,dot]
segnum = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
speedofsound = const(343) # centimeters
triggerpin = const(13)
echopin = const(12)
feetbuttonpin = const(14)
cmtoinch = const(0.39370079)

def getFeet(numInInches):
    s = "{0}".format(numInInches / 12)
    return (int(s[:s.find(".")]))
    
def getCentimeters(meters, totalCentimeters):
    return totalCentimeters - (meters * 100)

def centimetersToInches(centimeters):
    return centimeters * cmtoinch

def getInches(feet, totalInches):
    return totalInches - (feet * 12)

def getMeters(totalcentimeters):
    s = "{0}".format(totalcentimeters / 100)
    return int(s[:s.find(".")])

def paintnumber(val, digit, pins):
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
    
    time.sleep(.003)

    digitpin.high()

def printnumber(n, twodigits, twodigitpins):
    for d in twodigits:
        pin = Pin(d, Pin.OUT)
        pin.high()

    num = "{0}".format(n)
    i = len(num)-1
    d = 1

    while i >= 0 & d >= 0:
        val = segnum[int(num[i])]
        paintnumber(val, twodigits[d], twodigitpins)
        i -= 1
        d -= 1

def printfloat(f,digits, fourdigitpins):
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
                paintnumber(val, digits[d], fourdigitpins)
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
        for d in fourdigits:
            pin = Pin(d, Pin.OUT)
            pin.high()

        distancesample = 0
        
        for x in range(1000):
            samplemeasurement = not button.value()

            if(distancesample%15 == 0):
                distance = getdistancemeasure(trig, echo)

            meters = getMeters(distance)
            centimeters = getCentimeters(meters, distance)

            if samplemeasurement:
                print("Distance ({0} centimeters) in METERS ({1})) & CENTIMETERS ({2})".format(distance,meters,centimeters))
                
                for w in range(wait):
                    printnumber("{0}".format(meters), twodigits, twodigitpins)
                    printfloat(centimeters, fourdigits, fourdigitpins)
            else:
                totalInches = centimetersToInches(distance)
                feet = getFeet(totalInches)
                inches = getInches(feet, totalInches)
                print("Distance ({0} centimeters) in FEET ({1})) & INCHES ({2})".format(distance,feet,inches))

                for w in range(wait):
                    printnumber(feet, twodigits, twodigitpins)
                    printfloat(inches, fourdigits, fourdigitpins)
            
            distancesample += 1
        
    finally:
        #print("Finished")
        for d in twodigits:
            pin = Pin(d, Pin.OUT)
            pin.low()
        for d in fourdigits:
            pin = Pin(d, Pin.OUT)
            pin.low()
        for n in twodigitpins:
            pin = Pin(n, Pin.OUT)
            pin.low()
        for n in fourdigitpins:
            pin = Pin(n, Pin.OUT)
            pin.low()

if __name__ == '__main__':
	main()