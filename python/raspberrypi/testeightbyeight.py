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
import modules.eightbyeight as display

LED_rowpins = [9,14,8,12,1,7,2,5]
rowpins =     [7,11,13,19,21,23,35,37]
LED_colpins = [13,3,4,10,6,11,15,16]
colpins =     [8,10,12,16,18,22,24,26]

wait_time = 0.25

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
        print("starting rows")
        i = 0
        while i in range(len(rowpins)):
            GPIO.output(rowpins[i], GPIO.HIGH)
            time.sleep(wait_time)
            GPIO.output(rowpins[i], GPIO.LOW)
            i += 1

        time.sleep(wait_time)
        print("starting columns")
        for r in rowpins:
            GPIO.output(r, GPIO.HIGH)
        for c in colpins:
            GPIO.output(c, GPIO.HIGH)
        i = 0
        while i in range(len(colpins)):
            GPIO.output(colpins[i], GPIO.LOW)
            time.sleep(wait_time)
            GPIO.output(colpins[i], GPIO.HIGH)
            i += 1

        print("count off")

        row = 0
        for row in range(len(rowpins)):
            col = 0
            GPIO.output(rowpins[row], GPIO.HIGH)
            for col in range(len(colpins)):
                GPIO.output(colpins[col], GPIO.LOW)
                time.sleep(wait_time)
                GPIO.output(colpins[col], GPIO.HIGH)
            GPIO.output(rowpins[row], GPIO.LOW)

    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()