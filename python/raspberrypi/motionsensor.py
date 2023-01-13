import RPi.GPIO as GPIO
from datetime import datetime
import time

# Pin assignments
motion = 11 # GPIO17

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motion, GPIO.IN)

    print("Press Ctrl-C to quit'")

    try:
        state = False
        while True:
            # 15 minute wait
            
            if GPIO.input(motion) == GPIO.HIGH and state == False:
                print("motion detected at {0}".format(datetime.now()))
                state = True
            else:
                state = False
            time.sleep(.05)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()