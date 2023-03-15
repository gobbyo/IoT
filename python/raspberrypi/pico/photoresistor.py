from machine import Pin, PWM
import utime

# Max value of the ADC is 65535

ADCPin = const(26) #GP26

PicoVoltage = const(3.3)
ADC16BitRange = const(65536)

photoresistor = machine.ADC(ADCPin)
VoltagePerDegree =  PicoVoltage / ADC16BitRange 

while True:
    reading = photoresistor.read_u16()
    print("{:.2f}v".format(reading * VoltagePerDegree))
    utime.sleep(.125)