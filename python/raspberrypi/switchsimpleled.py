import RPi.GPIO as GPIO
import time

# Pin assignments (GPIO.BOARD)
button = 11 # GPIO17
led_green = 13 # GPIO27
led_red = 15 # GPIO22

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_green, GPIO.OUT)
    GPIO.setup(led_red, GPIO.OUT)
    GPIO.output(led_green, GPIO.LOW)
    GPIO.output(led_red, GPIO.LOW)

    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("Press Ctrl-C to quit'")
    last = 0
    cur = 0
    cnt = 0

    try:
        while True:
            cur = GPIO.input(button)
            if cur != last:
                if GPIO.input(button) == GPIO.LOW:
                    GPIO.output(led_green, GPIO.LOW)
                    GPIO.output(led_red, GPIO.HIGH)
                    cnt += 1
                    print("Button Released. Count = {0}".format(cnt))
                else:

                    GPIO.output(led_green, GPIO.HIGH)
                    GPIO.output(led_red, GPIO.LOW)
                    print("Button Pushed")
                last = cur
            time.sleep(0.01) # give the processor time to do other things
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()