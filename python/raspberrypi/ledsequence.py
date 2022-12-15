try:
    import time
    import random
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

INTERVAL = 0.125

def off(channel):
    GPIO.output(channel, GPIO.HIGH)
    print("Off")

def on(channel):
    GPIO.output(channel, GPIO.LOW)
    print("On")

def simpleSequence(LEDs):
    s = input("Provide a sequence (8): ").split(",")
    seq = []
    if len(s) <= 1:
        exit()
    for i in s:
        seq.append(int(i))
    
    i = 0
    while i < len(seq):
        on(LEDs[seq[i]-1])
        if i > 0:
            off(LEDs[seq[i-1]-1])
        i += 1
        time.sleep(INTERVAL)
    
    if i > 0:
        off(LEDs[seq[i-1]-1])

def loop(LEDs):
    i = random.randint(0,7)
    on(LEDs[i])
    time.sleep(INTERVAL)
    off(LEDs[i])
    return True

def main():
    LEDs = [4,5,12,13,20,21,22,23]

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LEDs, GPIO.OUT)
    GPIO.output(LEDs, GPIO.HIGH)

    while loop(LEDs):
        print("-----")
    
    GPIO.cleanup()

if __name__ == "__main__":
    main()