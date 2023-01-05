import RPi.GPIO as GPIO
import time

def main():
    pins = [32,10,12,16,18,22,24,26]

    GPIO.setmode(GPIO.BOARD)

    for p in pins:
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(p, GPIO.RISING)
    
    GPIO.add_event_callback(pins[0], callback_pin32)
    GPIO.add_event_callback(pins[1], callback_pin10)
    GPIO.add_event_callback(pins[2], callback_pin12)
    GPIO.add_event_callback(pins[3], callback_pin16)
    GPIO.add_event_callback(pins[4], callback_pin18)
    GPIO.add_event_callback(pins[5], callback_pin22)
    GPIO.add_event_callback(pins[6], callback_pin24)
    GPIO.add_event_callback(pins[7], callback_pin26) 

    print("Press Ctrl-C to quit'")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()