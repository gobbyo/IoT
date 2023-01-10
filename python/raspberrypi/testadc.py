import modules.ADC0832 as RPI_ADC0832

# Create an ADC0832 instance
adc = RPI_ADC0832.ADC0832()

# Specify which GPIO pins will be used
#adc.csPin = 17 # Default pin: 17
#adc.clkPin = 27 # Default pin: 27
#adc.doPin = 22 # Default pin: 23
#adc.diPin = 22 # Default pin: 24

# Print the current value of channel 0
valChannel0 = adc.read_adc(0)
print('Value of channel 0: ' +  str(valChannel0))

# Print the difference of both channel. You have to give which channel has the bigger value
valDifference = adc.read_adc_difference(0)
print('Difference: ' +  str(valDifference))