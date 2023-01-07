import RPi.GPIO as GPIO

def main():
    pins = [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,35,36,37,38,40]
    #invalid 27,28
    GPIO.setmode(GPIO.BOARD)
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)

    print("Press Ctrl-C to quit'")

    try:
        s = input("type anything to exit")
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()