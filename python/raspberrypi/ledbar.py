import RPi.GPIO as GPIO
import time

def main():
    LED_pins = [8,12,16,18,22,24,26,32,36,38]

    GPIO.setmode(GPIO.BOARD)

    for p in LED_pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)

    try:
        on = True
        while True:
            for p in LED_pins:
                if on:
                    GPIO.output(p, GPIO.LOW)
                else:
                    GPIO.output(p, GPIO.HIGH)
                time.sleep(0.25)
            if(on):
                on = False
            else:
                on = True
            time.sleep(2)
    except KeyboardInterrupt:
        print("Program shut down")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()