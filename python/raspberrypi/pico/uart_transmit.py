from machine import UART, Pin
import time

def main():
    led = Pin(25, Pin.OUT)
    try:
        uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
        uart.init(9600, bits=8, parity=None, stop=1)
        print("UART is configured as : ", uart)
        while True:
            #baudrates = [9600, 19200, 38400, 57600, 115200]

            uart.write('On')
            led.on()
            time.sleep(1)
            #s = uart.readline().decode('utf-8')
            #print("received = {0}".format(s))
            uart.write('Off')
            led.off()
            time.sleep(1)
            #s = uart.readline().decode('utf-8')
            #print("received = {0}".format(s))
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        led.low()
        print('Done')

if __name__ == "__main__":
    main()
