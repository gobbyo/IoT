import RPi.GPIO as GPIO
from threading import Timer, Lock
import time

btn_in = 11
btn_out = 12
led_rise = 13
led_fall = 15

class count:
    def __init__(self):
        self.i = 0
        self.lock = Lock()

cnt = count()

def my_callback_rise(channel):
    GPIO.output(led_rise, GPIO.HIGH)
    GPIO.output(led_fall, GPIO.LOW)

    print("{rise}:On {fall}:Off".format(rise=led_rise,fall=led_fall))
    
def my_callback_fall(channel):
    GPIO.output(led_rise, GPIO.LOW)
    GPIO.output(led_fall, GPIO.HIGH)

    t = Timer(interval=1.0, function=turn_led_off)
    t.start()

    cnt.lock.acquire(True, timeout=1.0)
    cnt.i += 1
    cnt.lock.release()

    print("{rise}:Off {fall}:On. Click count:{i}".format(rise=led_rise,fall=led_fall,i=cnt.i))

def turn_led_off():
    GPIO.output(led_fall, GPIO.LOW)
    GPIO.output(led_rise, GPIO.LOW)
    print("{rise}:Off {fall}:Off".format(rise=led_rise,fall=led_fall))

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_rise, GPIO.OUT)
    GPIO.setup(led_fall, GPIO.OUT)
    GPIO.output(led_rise, GPIO.LOW)
    GPIO.output(led_fall, GPIO.LOW)

    GPIO.setup(btn_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(btn_out, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(btn_in, GPIO.RISING, my_callback_rise, bouncetime=100)
    GPIO.add_event_detect(btn_out, GPIO.FALLING, my_callback_fall, bouncetime=100)

    print("Press Ctrl-C to quit'")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()