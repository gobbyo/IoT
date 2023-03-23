from machine import Pin
import time

def main():
    picopin = 25
    #picopin = "LED"
    try:
        button=Pin(15,Pin.IN,Pin.PULL_UP)
        pin=Pin(picopin,Pin.OUT)

        print("starting program")
        while True:
            if button.value() == 1:
                pin.high()
            else:
                pin.low()
            time.sleep(.025)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        print("Cleaning up and shutting down")
if __name__ == '__main__':
    main()