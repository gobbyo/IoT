from machine import Pin, ADC

ADCLowVoltPin = 26 #GP26
ADCMaxVoltPin = 27 #GP27
PicoMaxADCVoltage = 3.3
ADC16BitRange = 65536
LEDMeterRange = 10

def main():
    batterySizeL = 1.5
    batterySizeH = 3.0
    LEDSegDisplay = []

    try:
        batteryLowVoltage = ADC(ADCLowVoltPin)
        batteryHighVoltage = ADC(ADCMaxVoltPin)
        voltagePerDegree =  PicoMaxADCVoltage / ADC16BitRange

        for i in range(LEDMeterRange):
            LEDSegDisplay.append(Pin(i+1, Pin.OUT))
        
        while True:
            percentageOfBattery = 0
            batteryVoltage = voltagePerDegree * batteryLowVoltage.read_u16()
            #print("Battery Voltage: ", batteryVoltage)
            percentageOfBattery = batteryVoltage/batterySizeL
            #print("Percentage of batterySizeL: ", percentageOfBattery)
            if percentageOfBattery*10 < 1:
                batteryVoltage = voltagePerDegree * batteryHighVoltage.read_u16()
                percentageOfBattery = batteryVoltage/batterySizeH
                #print("Percentage of batterySizeH: ", percentageOfBattery)
            
            LEDdisplay = int(percentageOfBattery*LEDMeterRange)
            #print("LED Display: ", LEDdisplay)
            if LEDdisplay > LEDMeterRange:
                LEDdisplay = LEDMeterRange

            for i in range(LEDMeterRange):
                if i < LEDdisplay:
                    LEDSegDisplay[i].high()
                else:
                    LEDSegDisplay[i].low()

    except KeyboardInterrupt:
        print("stopping program")
    
    finally:
        print("Graceful exit")
        for i in range(LEDMeterRange):
            LEDSegDisplay[i].low()

if __name__ == '__main__':
    main()