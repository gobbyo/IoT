import RPi.GPIO as GPIO
import time

def main():
    LED_pins = [8,12,14,16,18,20,22,26,28]

    GPIO.setmode(GPIO.BOARD)

    for p in LED_pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

    try:
        on = True
        while True:
            for p in LED_pins:
                if on:
                    GPIO.output(LED_channel, GPIO.HIGH)
                else:
                    GPIO.output(LED_channel, GPIO.LOW)
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