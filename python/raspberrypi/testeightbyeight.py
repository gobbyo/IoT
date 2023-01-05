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

LED_rowpins = [9,14,8,12,1,7,2,5]
LED_colpins = [13,3,4,10,6,11,15,16]
rowpins = [7,11,13,15,29,31,33,35]
colpins = [16,18,22,24,32,36,38,40]

def main():

    GPIO.setmode(GPIO.BOARD)

    for r in rowpins:
        GPIO.setup(r, GPIO.OUT)
        GPIO.output(r, GPIO.LOW)
    
    for c in colpins:
        GPIO.setup(c, GPIO.OUT)
        GPIO.output(c, GPIO.LOW)

    print("Press Ctrl-C to quit'")

    try:
        print("starting")
        i = 0
        while i in range(8):
            GPIO.output(rowpins[i], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(rowpins[i], GPIO.LOW)
            i += 1
                
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()