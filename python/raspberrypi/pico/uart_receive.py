from machine import UART, Pin
import time

def main():
    #baudrates = [9600, 19200, 38400, 57600, 115200]
    led = Pin(25, Pin.OUT) 
    try:
        uart = UART(0, baudrate=115200, rx=Pin(1))
        uart.init(9600, bits=8, parity=None, stop=1)
        while True:
            if uart.any():
                s = uart.readline().decode('utf-8')
                print(s)
                if s == 'On':
                    led.on()
                else:
                    led.off()
            else:
                pass
            
            time.sleep(.05)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        led.low()
        print('Done')
if __name__ == "__main__":
    main()
