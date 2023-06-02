from machine import Pin, PWM
import time

class sg90:
    __servo_pwm_freq = 50
    __min_u16_duty = 1640 - 2 # offset for correction
    __max_u16_duty = 7864 - 0  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001

    def __init__(self, pin):
        self.__initialise(pin)

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

def main():
    servo = sg90(22)
    i = 0
    while i < 90:
        i += 10
        print("angle = {0}".format(i))
        servo.move(i)
        time.sleep(.5)
    
    i = 90
    while i > 0:
        i -= 10
        print("angle = {0}".format(i))
        servo.move(i)
        time.sleep(.5)

    i = 0
    while i < 180:
        i += 30        
        print("angle = {0}".format(i))
        servo.move(i)
        time.sleep(.5)

    i = 180
    while i > 0:
        i -= 45
        print("angle = {0}".format(i))
        servo.move(i)
        time.sleep(.5)


if __name__ == '__main__':
    main()