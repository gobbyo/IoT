import keyboard

def run_sample():
    while cont:
        i = 1
    print("Graceful exit")

def on_keypressed(e):
    print('{0}({1})'.format(e.name, hex(e.scan_code)))

def main():
    global cont
    cont = True
    keyboard.on_press(on_keypressed)
    print("Press Ctrl-C to quit'")

    try:
        run_sample()
    except KeyboardInterrupt:
        print("Program shut down by user")
    finally:
        print("Shutting down")

if __name__ == "__main__":
    main()