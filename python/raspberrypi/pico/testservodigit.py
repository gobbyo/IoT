from servodisplay import servoDigitDisplay
import time

extend = [5,10,10,10,0,10,10]
retract = [110,115,110,110,100,115,115]
servospeed = 0.03

def main():
    digit = servoDigitDisplay()
    digit.servospeed = servospeed

    for i in range(0,7):
        digit.extendAngles[i] = extend[i]
        digit.retractAngles[i] = retract[i]

    try:
        while True:
            for i in range(0,10):
                print("Number {0}".format(i))
                digit.paintNumber(i,True)
                time.sleep(60)
                digit.paintNumber(i,False)

    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        digit.__del__()
        print('Done')

if __name__ == '__main__':
    main()