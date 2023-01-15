from modules.ADC0832joystick import ADC0832joystick
import RPi.GPIO as GPIO

btn = 15# Define button pin

def getResult(ADC):#get joystick result
	if ADC.getResult(1) == 0:
		return 1 # up
	if ADC.getResult(1) == 255:
		return 2 # down
	if ADC.getResult(0) == 0:
		return 3 # left
	if ADC.getResult(0) == 255:
		return 4 # right

def button_pushed(channel):
	print("Button pushed gpio_pin={0}".format(channel))

def main():
	print("ctrl-c to quit")
	try:
		ADC = ADC0832joystick()
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		#joystick button requires a lot of bouncetime to prevent duplicates
		GPIO.add_event_detect(btn, GPIO.RISING, button_pushed, bouncetime=500)
		global state
		state = ['up', 'down', 'left', 'right']
		prev = ""
		while True:
			tmp = getResult(ADC)
			if tmp != None and prev != tmp:
				print(state[tmp-1])
				prev = tmp
	except KeyboardInterrupt:
		print("")
		print("exiting program")
	finally:
		GPIO.cleanup()

if __name__ == '__main__':
	main()
