import modules.ADC0832 as RPI_ADC0832
import time

def main():

    # Create an ADC0832 instance
    adc = RPI_ADC0832.ADC0832()

    #adc.csPin = 17 # Default pin: 17
    #adc.clkPin = 27 # Default pin: 27
    #adc.doPin = 23 # Default pin: 23
    #adc.diPin = 24 # Default pin: 24
    prev = 0
    
    try:
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
            if prev != percent:
                print('{0}%'.format(percent))
                prev = percent
            time.sleep(.5)
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        adc.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()