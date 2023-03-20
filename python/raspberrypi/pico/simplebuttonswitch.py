from machine import Pin
import time

def main():
    #pico = pin 25 #
    #picow = "LED"
    try:
        button=Pin(2,Pin.IN, Pin.PULL_DOWN)

        print("starting program")
        while True:
            if button.value() == 1:
                print("button.value({0})".format(button.value()))
            time.sleep(.25)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        print("Cleaning up and shutting down")
if __name__ == '__main__':
    main()