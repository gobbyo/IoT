import RPi.GPIO as GPIO
import time

morse = dict(A='.-',B='-...',C='-.-.',D='-..',E='.',F='..-.',G='--.',H='....',I='..',J='.---',K='-.-',L='.-..',M='--',N='-.',O='---',P='.--.',Q='--.-',R='.-.',S='...',T='-',U='..-',V='...-',W='.--',X='-..-',Y='-.--',Z='--..')
dotlength = 0.15
dashlength = 0.5
wordpause = .75
letterpause = 0.25
morsepause = 0.15
pin = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)

def play(word):
    for c in word:
        if c in morse.keys():
            m = morse[c]
            print("{0}:{1}".format(c,m))
            for i in m:
                GPIO.output(pin, GPIO.LOW)
                if i == '.':
                    time.sleep(dotlength)
                else:
                    time.sleep(dashlength)
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(morsepause)
        else:
            print("{0} not in dictionary".format(c))
        time.sleep(letterpause)
            
def main():
    try:
        print("Type only a-z, A-Z, or ctrl-c to exit")
        while True:
            sentence = input("Sentence or word: ")
            if len(sentence) > 1:
                words = sentence.split(" ")
                if len(words) > 1:
                    for word in words:
                        play(word.upper())
                        print("")
                        time.sleep(wordpause)
                else:
                    play(sentence.upper())
    except KeyboardInterrupt:
        print("ctrl-c command.")
    finally:
        GPIO.cleanup()
        print("Exiting program.")

if __name__ == "__main__":
    main()
