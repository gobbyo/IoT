from machine import Pin

#defaults
latchpin = const(7) #RCLK
clockpin = const(6) #SRCLK
datapin = const(8) #SER

class shiftregister():
    def __init__(self) -> None:
        self.register = []
        self.latch = Pin(latchpin, Pin.OUT)
        self.clock = Pin(clockpin, Pin.OUT)
        self.data = Pin(datapin, Pin.OUT)

    def set_pins(self, latch_pin, clock_pin, data_pin):
        self.latch.low()
        self.clock.low()
        self.data.low()
        del(self.latch)
        del(self.clock)
        del(self.data)
        self.latch = Pin(latch_pin, Pin.OUT)
        self.clock = Pin(clock_pin, Pin.OUT)
        self.data = Pin(data_pin, Pin.OUT)
        
    def set_registerSize(self,size):
        for i in range(size):
            self.register.append(0)

    def setregister(self):
        #open latch for data
        self.clock.low()
        self.latch.low()
        self.clock.high()

        #load data in register
        for i in range(len(self.register)-1, -1, -1):
            self.clock.low()
            if self.register[i] == 1:
                self.data.high()
            else:
                self.data.low()
            self.clock.high()

        #close latch for data
        self.clock.low()
        self.latch.high()
        self.clock.high()