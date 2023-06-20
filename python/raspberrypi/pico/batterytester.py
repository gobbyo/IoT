from machine import Pin, ADC
import shiftregister
import time

ADCPin = 28 #GP28
PicoMaxADCVoltage = 3.3
ADC16BitRange = 65536
LEDMeterRange = 10
ClearRegister = [0,0,0,0,0,0,0,0,0,0]

def main():
    batterySize = 1.5

    try:
        battery = ADC(ADCPin)
        voltagePerDegree =  PicoMaxADCVoltage / ADC16BitRange

        r = shiftregister.shiftregister()
        r.set_registerSize(LEDMeterRange)
        r.register = ClearRegister
        r.setregister()

        while True:
            batteryvoltage = voltagePerDegree * battery.read_u16()
            #print("batteryvoltage = {:.2f}".format(batteryvoltage))
            percentageOfBattery = batteryvoltage/batterySize
            LEDdisplay = round(percentageOfBattery*LEDMeterRange)
            
            if LEDdisplay <= LEDMeterRange:
                #set the shift register
                i = 0
                while i < LEDMeterRange:
                    if i < LEDdisplay:
                        r.register[i] = 1
                    else:
                        r.register[i] = 0
                    i += 1
                #print("LEDdisplay = {0}, battery voltage = {1}, register = {2}".format(LEDdisplay, batteryvoltage, r.register))
                r.setregister()

    except KeyboardInterrupt:
        print("stopping program")

    finally:
        print("Graceful exit")

if __name__ == '__main__':
    main()