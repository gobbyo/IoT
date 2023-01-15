import RPi.GPIO as GPIO
import time

MotorPin_A         = 38
MotorPin_B         = 40

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MotorPin_A,GPIO.OUT)
    GPIO.setup(MotorPin_B,GPIO.OUT)

    try:
        GPIO.output(MotorPin_A,GPIO.HIGH)
        GPIO.output(MotorPin_B,GPIO.LOW)
        time.sleep(1)
        GPIO.output(MotorPin_B,GPIO.HIGH)
        GPIO.output(MotorPin_A,GPIO.LOW)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Program shut down")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()