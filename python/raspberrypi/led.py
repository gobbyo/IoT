try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

def printInfo():
    print("MANUFACTURER = %s"%GPIO.RPI_INFO['MANUFACTURER'])
    print("PROCESSOR = %s"%GPIO.RPI_INFO['PROCESSOR'])
    print("-------")

def checkChannel(channel):
    if GPIO.HIGH == GPIO.input(channel):
        print("LED channel says ON")
    else:
        print("LED channel says OFF")

def on(channel):
    GPIO.output(channel, GPIO.HIGH)
    print("On")

def off(channel):
    GPIO.output(channel, GPIO.LOW)
    print("Off")

def loop(channels):
    if "N" == input("Continue? Y/N: "):
        return False
    channel = int(input("Select channel to turn on or off {0}: ".format(channels)))
    if "On" == input("Choose a command (On, Off): "):
        on(channel)
    else:
        off(channel)
    
    return True

def main():

    i = 0
    LEDs = []

    GPIO.setmode(GPIO.BCM)
    total = int(input("Number of LEDs: "))
    if total < 1:
        GPIO.cleanup()
        exit()

    while i < total:
        LEDs.append(int(input("Channel for {0}: ".format(i+1))))
        i += 1

    GPIO.setup(LEDs, GPIO.OUT)

    while loop(LEDs):
        print("-----")
    
    GPIO.cleanup()

if __name__ == "__main__":
    main()