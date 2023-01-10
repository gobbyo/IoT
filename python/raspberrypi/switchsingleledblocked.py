import RPi.GPIO as GPIO
import time

button = 11 # GPIO17
led_green = 13 # GPIO27
led_fall = 15 # GPIO22

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_green, GPIO.OUT)
    GPIO.setup(led_fall, GPIO.OUT)
    GPIO.output(led_green, GPIO.LOW)
    GPIO.output(led_fall, GPIO.LOW)

    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("Press Ctrl-C to quit'")
    cnt = 0
    result = 0

    try:
        while True:
            result = GPIO.wait_for_edge(button, GPIO.RISING, timeout=5000)
            if result is None:
                print('Timeout waiting for button to be pushed')
            else:
                GPIO.output(led_green, GPIO.HIGH)
                GPIO.output(led_fall, GPIO.LOW)
                print("Button Pushed")
                result = GPIO.wait_for_edge(button, GPIO.FALLING, timeout=5000)
                if result is None:
                    print('Timeout waiting for button to be released')
                else:
                    GPIO.output(led_green, GPIO.LOW)
                    GPIO.output(led_fall, GPIO.HIGH)
                    cnt += 1
                    print("Button Released. Count = {0}".format(cnt))
            time.sleep(0.01) # give the processor time to do other things
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()