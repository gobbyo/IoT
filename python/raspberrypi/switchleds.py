import RPi.GPIO as GPIO
from threading import Timer, Lock
import time

btn_in = 11 # GPIO17
btn_out = 12 # GPIO18
led_green = 13 # GPIO27
led_red = 15 # GPIO22

class count:
    def __init__(self):
        self.i = 0
        self.lock = Lock()

t = None
cnt = count()

def button_pushed(channel):
    GPIO.output(led_green, GPIO.HIGH)
    GPIO.output(led_red, GPIO.LOW)
    print("Button Pushed")
    
def button_released(channel):
    GPIO.output(led_green, GPIO.LOW)
    GPIO.output(led_red, GPIO.HIGH)

    if t != None:
        t.cancel()
        time.sleep(.01)
    
    t = Timer(interval=1.0, function=turn_led_off)
    t.start()

    cnt.lock.acquire(True, timeout=1.0)
    cnt.i += 1
    cnt.lock.release()

    print("Button Released. Count = {i}".format(rise=led_green,fall=led_red,i=cnt.i))

def turn_led_off():
    GPIO.output(led_red, GPIO.LOW)
    GPIO.output(led_green, GPIO.LOW)
    print("All LEDs Off")

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_green, GPIO.OUT)
    GPIO.setup(led_red, GPIO.OUT)
    GPIO.output(led_green, GPIO.LOW)
    GPIO.output(led_red, GPIO.LOW)

    GPIO.setup(btn_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(btn_out, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(btn_in, GPIO.RISING, button_pushed, bouncetime=200)
    GPIO.add_event_detect(btn_out, GPIO.FALLING, button_released, bouncetime=200)

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