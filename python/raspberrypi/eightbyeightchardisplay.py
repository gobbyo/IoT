#			C	o	l	u	m	n	s	
#		Pin	13	3	4	10	6	11	15	16
#		9	1	2	3	4	5	6	7	8
#	R	14	9	10	11	12	13	14	15	16
#	o	8	17	18	19	20	21	22	23	24
#	w	12	25	26	27	28	29	30	31	32
#	s	1	33	34	35	36	37	38	39	40
#		7	41	42	43	44	45	46	47	48
#		2	49	50	51	52	53	54	55	56
#		5	57	58	59	60	61	62	63	64

import RPi.GPIO as GPIO
import time
import modules.eightbyeight as charfont

rowpins =     [7,11,13,19,21,23,35,37]
colpins =     [8,10,12,16,18,22,24,26]

wait_time = 0.002

def paintscreen(buffer):
    for dur in range(15):
        for colpin in colpins:
            GPIO.output(colpin, GPIO.HIGH)
        row = 0
        for val in buffer:
            GPIO.output(rowpins[row],GPIO.HIGH)
            i = 0
            for colpin in colpins:
                t = (val & (0x01 << i)) >> i
                if t > 0:
                    GPIO.output(colpin,GPIO.LOW)
                i += 1
            time.sleep(wait_time)
            
            for colpin in colpins:
                GPIO.output(colpin, GPIO.HIGH)
            GPIO.output(rowpins[row],GPIO.LOW)
            row += 1

def main():

    GPIO.setmode(GPIO.BOARD)

    for rowpin in rowpins:
        GPIO.setup(rowpin, GPIO.OUT)
        GPIO.output(rowpin, GPIO.LOW)
    
    for colpin in colpins:
        GPIO.setup(colpin, GPIO.OUT)
        GPIO.output(colpin, GPIO.LOW)

    print("Press Ctrl-C to quit'")

    try:
        print("display character")
        i = 35
        while i < 128:
            paintscreen(charfont.font8x8_basic[i])
            i += 1

    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()