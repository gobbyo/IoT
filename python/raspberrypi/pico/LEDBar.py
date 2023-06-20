from machine import Pin
import shiftregister
import time

def testLEDBar(shiftreg, pausetime):
    shiftreg.setregister()
    for i in range(len(shiftreg.register)):
        shiftreg.register[i] = 1
        shiftreg.setregister()
        time.sleep(pausetime)
    while i >= 0:
        shiftreg.register[i] = 0
        shiftreg.setregister()
        time.sleep(pausetime)
        i -= 1
    shiftreg.register = [0,0,0,0,0,0,0,0,0,0]
    shiftreg.setregister()
    
def main():
    try:
        onboardLED = Pin(25,Pin.OUT)
        onboardLED.high()
        time.sleep(2)
        onboardLED.low()

        r = shiftregister.shiftregister()
        r.set_registerSize(10)

        while True:
            testLEDBar(r,0.1)
            time.sleep(.25)
    except KeyboardInterrupt:
        print("stopping program")

    finally:
        print("Graceful exit")
if __name__ == '__main__':
    main()