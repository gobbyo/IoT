import RPi.GPIO as GPIO
import time

class ADC0832joystick(object):

	def __init__(self):
		# Initialize pin numbers
		self.csPin = 11 # BCM 17
		self.clkPin = 13 # BCM 27
		self.dioPin = 16 # BCM 23
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)# Number GPIOs by its physical location
		GPIO.setup(self.csPin, GPIO.OUT)# Set pins' mode is output
		GPIO.setup(self.clkPin, GPIO.OUT)# Set pins' mode is output

	# using channel = 0 as default for backwards compatibility
	def getResult(self, channel=0):# Get ADC result, input channal
		timingOffset = 1.05
		GPIO.setup(self.dioPin, GPIO.OUT)
		GPIO.output(self.csPin, 0)

		GPIO.output(self.clkPin, 0)
		GPIO.output(self.dioPin, 1)
		time.sleep(0.00025 * timingOffset)
		GPIO.output(self.clkPin, 1)
		time.sleep(0.00009 * timingOffset)
		GPIO.output(self.clkPin, 0)

		GPIO.output(self.dioPin, 1)
		time.sleep(0.00025 * timingOffset)
		GPIO.output(self.clkPin, 1)
		time.sleep(0.00009 * timingOffset)
		GPIO.output(self.clkPin, 0)

		GPIO.output(self.dioPin, channel);
		time.sleep(0.00009 * timingOffset)

		GPIO.output(self.clkPin, 1)
		GPIO.output(self.dioPin, 1)
		time.sleep(0.00025 * timingOffset)
		GPIO.output(self.clkPin, 0)
		GPIO.output(self.dioPin, 1)
		time.sleep(0.00009 * timingOffset)

		dat1 = 0
		for i in range(0, 8):
			GPIO.output(self.clkPin, 1)
			time.sleep(0.00009 * timingOffset)
			GPIO.output(self.clkPin, 0)
			time.sleep(0.0015 * timingOffset)
			GPIO.setup(self.dioPin, GPIO.IN)
			dat1 = dat1 << 1 | GPIO.input(self.dioPin)  

		dat2 = 0
		for i in range(0, 8):
			dat2 = dat2 | GPIO.input(self.dioPin) << i
			GPIO.output(self.clkPin, 1)
			time.sleep(0.00009 * timingOffset)
			GPIO.output(self.clkPin, 0); 
			time.sleep(0.0006 * timingOffset)

		GPIO.output(self.csPin, 1)
		GPIO.setup(self.dioPin, GPIO.OUT)

		if dat1 == dat2:
			return dat1
		else:
			return 0