from machine import Pin, PWM
import time
import math

segpins = [16,17,18,19,20,21,22]
extendangles = [10,15,0,15,0,0,0]
retractangles = [100,100,85,90,90,90,90]
switchpins = [13,14,15,12]

class sg90:
    __servo_pwm_freq = 50
    __min_u16_duty = 1640 - 2 # offset for correction
    __max_u16_duty = 7864 - 0  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001

    def __init__(self, pin):
        self.__initialise(pin)
    
    def __del__(self):
        self.move(0)

    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.__max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)

    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted sg90 adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty

    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)

def getArray(val):
    a = [0,0,0,0,0,0,0,0]
    i = 0
    for s in a:
        a[i] = (val & (0x01 << i)) >> i
        i += 1
    return a

def extend(servo,angle):
    i = 90
    while i >= angle:
        i -= 5
        #print("angle = {0}".format(i))
        servo.move(i)
        time.sleep(.05)

def retract(servo,angle):
    i = 0
    while i <= angle:
        i += 5
        #print("angle = {0}".format(i))
        servo.move(i)
        time.sleep(.05)

def main():
    seg = []
    print("Start")
    for i in segpins:
        seg.append(sg90(i))

    switch = []
    for i in switchpins:
        pin = Pin(i, Pin.OUT)
        pin.off()
        switch.append(pin)

    try:
        for i in range(0,1):
            print("\nIteration {0}".format(i+1))
            print("Extending...")
            #switch
            r = 4
            for j in range(0,r):
                print("Pin {0}".format(segpins[j]))
                i = int(math.fmod(j,len(switch)))
                switch[i].on()
                extend(seg[j],extendangles[j])
                switch[i].off()

            time.sleep(1)

            print("Retracting...")
            for j in range(0,r):
                print("Pin {0}".format(segpins[j]))
                i = int(math.fmod(j,len(switch)))
                switch[i].on()
                retract(seg[j],retractangles[j])
                switch[i].off()

            time.sleep(1)

    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        print('Done')

if __name__ == '__main__':
    main()