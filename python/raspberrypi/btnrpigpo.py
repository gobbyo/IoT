import RPi.GPIO as GPIO

Btn = 23 
Red = 12
Buz = 18

def setup():
    GPIO.setmode(GPIO.BCM)   # Numbers GPIOs by physical location
    GPIO.setup(Red, GPIO.OUT)   # Set Red pin mode is output
    GPIO.setup(Buz, GPIO.OUT)   # Set Buzzer's mode is output
    GPIO.setup(Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set Btn's mode is input, and pull up to high level(3.3V)
    GPIO.output(Red, GPIO.LOW)
    GPIO.output(Buz, GPIO.LOW)

def loop():
    state = False
    while True:
        if GPIO.input(Btn) == GPIO.LOW: # Check whether the button is pressed or not.
            if state == False:
                GPIO.output(Red, GPIO.HIGH)
                GPIO.output(Buz, GPIO.HIGH)
                print('...led on')
                state = True
        else:
            GPIO.output(Red, GPIO.LOW)
            GPIO.output(Buz, GPIO.LOW)
            state = False

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()  

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()