from machine import Pin, PWM
import distancehelper
import time

nano = const(0.00000001)
speedofsound = const(0.00343) # centimeters per second
triggerpin = const(13)
echopin = const(12)

def LEDindicator():
    led = PWM(Pin(25))
    led.freq(1000)      # Set the frequency value
    led_value = 0       #LED brightness initial value
    led_speed = 5      # Change brightness in increments of 5

    for i in range(75):                            
        led_value += led_speed           
        led.duty_u16(int(led_value * 500))     # Set the duty cycle, between 0-65535
        time.sleep_ms(100)
        if led_value >= 100:
            led_value = 100
            led_speed = -5
        elif led_value <= 0:
            led_value = 0
            led_speed = 5
    
    led.duty_u16(int(0))

def main():
    # printfloat(12.75)
    
    trig = Pin(triggerpin, Pin.OUT)
    echo = Pin(echopin, Pin.IN, Pin.PULL_DOWN)

    try:
        for i in range(4):
            receive = 0
            send = 0

            trig.low()
            time.sleep_ms(2)
            trig.high()
            time.sleep_ms(5)
            trig.low()
            
            while echo.value() == 0:
                pass
            send = time.ticks_ms()

            while echo.value() == 1:
                pass
            receive = time.ticks_ms()

            timepassed = receive - send
            distanceincentemeters = (timepassed * speedofsound) / 2

            totalInches = distancehelper.centimetersToInches(distanceincentemeters)
            feet = distancehelper.getFeet(totalInches)
            inches = distancehelper.getInches(feet, totalInches)
            print("{0} feet {1} inches".format(feet,inches))
            time.sleep(1)
        
    finally:
        LEDindicator()
        print("Finished")


if __name__ == '__main__':
	main()