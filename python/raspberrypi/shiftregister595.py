import RPi.GPIO as GPIO
import time

#   2 digit 7 segmented LED
#
#       digit 1        digit 2        
#        _a_            _a_   
#     f |_g_| b      f |_g_| b
#     e |___| c _h   e |___| c _h
#         d              d       
#

# num   hgfe dcba   hex
#
# 0 = 	0011 1111   0x3F
# 1 =	0000 0110   0x06
# 2 =	0101 1011   0x5B
# 3 =	0100 1111   0x4F
# 4 =	0110 0110   0x66
# 5 =	0110 1101   0x6D
# 6 =	0111 1101   0x7D
# 7 =	0000 0111   0x07
# 8 =   0111 1111   0x7F
# 9 =   0110 0111   0x67

def shift_update(input,data,clock,latch):
  #put latch down to start data sending
  GPIO.output(clock,0)
  GPIO.output(latch,0)
  GPIO.output(clock,1)

  #load data in reverse order
  for i in range(7, -1, -1):
    GPIO.output(clock,0)
    GPIO.output(data, input[i])
    GPIO.output(clock,1)

  #put latch up to store data on register
  GPIO.output(clock,0)
  GPIO.output(latch,1)
  GPIO.output(clock,1)

def getArray(val):
    a = [0,0,0,0,0,0,0,0]
    i = 0
    for s in a:
        a[i] = (val & (0x01 << i)) >> i
        i += 1
    #print(a)
    return a

def main():
    segnum = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67,0]
    latch = 38 #RCLK
    clock = 36 #SRCLK
    data = 40 #SER

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(latch, GPIO.OUT)
    GPIO.setup(clock, GPIO.OUT)
    GPIO.setup(data, GPIO.OUT)

    print("Press Ctrl-C to quit'")

    try:
        while True:
            for s in segnum:
                shift_update(getArray(s),data,clock,latch)
                time.sleep(.5)

    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        GPIO.cleanup()
        print("Cleaning up and shutting down")

if __name__ == "__main__":
    main()