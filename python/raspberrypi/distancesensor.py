import RPi.GPIO as GPIO
import time

speedofsound = 343 # meters per second
nano = 0.00000001
inset = 1.32
trig = 38
echo = 40

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(echo, GPIO.IN)

    try:
            while True:
                GPIO.output(trig, GPIO.HIGH)
                time.sleep(0.000001)
                GPIO.output(trig, GPIO.LOW)

                while GPIO.input(echo) == GPIO.LOW:
                    pass
                send = time.time_ns()

                while GPIO.input(echo) == GPIO.HIGH:
                    pass
                receive = time.time_ns()
                m_per_sec = speedofsound * ((receive - send) * nano)
                m_per_sec /= 2 # there and back again
                distance = (m_per_sec * 10) - inset
                print("{:.1f} centimeters".format(distance))
                time.sleep(1)

    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()