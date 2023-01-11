import modules.ADC0832 as RPI_ADC0832
import time

def main():

    # Create an ADC0832 instance
    adc = RPI_ADC0832.ADC0832()

    # Specify which GPIO pins will be used
    #adc.csPin = 17 # Default pin: 17
    #adc.clkPin = 27 # Default pin: 27
    #adc.doPin = 23 # Default pin: 23
    #adc.diPin = 24 # Default pin: 24
    prev = 0
    
    while True:
        val = adc.read_adc(0)
        ch0 = adc.read_adc(0)
        ch1 = adc.read_adc(1)
        if ch0 > ch1:
            val = ch0
        else:
            val = ch1
        
        percent = round((val/255) * 100)
        if prev != percent:
            print('{0}%'.format(percent))
            prev = percent
        time.sleep(.5)

if __name__ == "__main__":
    main()