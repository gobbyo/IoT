import RPi.GPIO as GPIO
import time

def main():
    pin = 37

    GPIO.setmode(GPIO.Board)
    GPIO.setup(LED_channel, GPIO.OUT)
    GPIO.output(LED_channel, GPIO.LOW)

    print("Press Ctrl-C to quit'")

    try:
        GPIO.PWM(LED_channel, 440)
        time.sleep(1)
        GPIO.output(LED_channel, GPIO.LOW)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()