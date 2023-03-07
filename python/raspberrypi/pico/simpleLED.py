from machine import Pin
from time import sleep

def main():
    pin=Pin(25,Pin.OUT)

    print("starting program")
    for i in range(6):
        pin.high()
        sleep(.5)
        pin.low()
        sleep(.5)
    
    print("ending program")

if __name__ == '__main__':
    main()