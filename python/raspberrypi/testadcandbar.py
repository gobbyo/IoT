import RPi.GPIO as GPIO
import modules.ADC0832 as RPI_ADC0832
import time

def main():

    # Create an ADC0832 instance
    adc = RPI_ADC0832.ADC0832()
    #adc.csPin = 17 # Default pin: 17
    #adc.clkPin = 27 # Default pin: 27
    #adc.doPin = 23 # Default pin: 23
    #adc.diPin = 24 # Default pin: 24

    LEDbar = [21,20,16,12,7,8,25,18,15,14]
    prev = 0
    
    try:
        for p in LEDbar:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, GPIO.LOW)
        print("Type ctrl-c to quit")
        print("Light intensity from 0 to 100%:")
        while True:
            val = 0
            ch0 = adc.read_adc(0)
            ch1 = adc.read_adc(1)
            #get the higher value
            if ch0 > ch1:
                val = ch0
            else:
                val = ch1
            
            percent = round((val/255) * 100)
            num = round(percent/10)
            if prev != percent:
                print('{0}% {1}'.format(percent, num))
                prev = percent
            
            val = 0
            num = round(percent/10)
            while val < num:
                GPIO.output(LEDbar[val], GPIO.HIGH)
                val += 1
            while val < len(LEDbar):
                GPIO.output(LEDbar[val], GPIO.LOW)
                val += 1
            time.sleep(.5)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        adc.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()