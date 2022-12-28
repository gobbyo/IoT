import RPi.GPIO as GPIO

def main():
    LED_channel = 17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_channel, GPIO.OUT)
    GPIO.output(LED_channel, GPIO.LOW)

    print("Press Ctrl-C to quit'")

    try:
        while True:
            s = input("Type 'On' or 'Off': ")
            if s == 'On':
                GPIO.output(LED_channel, GPIO.HIGH)
                print("On")
            else:
                GPIO.output(LED_channel, GPIO.LOW)
                print("Off")
            print("-----")
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()