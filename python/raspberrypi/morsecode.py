import time
import winsound

morse = dict(A='.-',B='-…',C='-.-.',D='-..',E='.',F='..-.',G='--.',H='….',I='..',J='.---',K='-.-',L='.-..',M='--',N='-.',O='---',P='.--.',Q='--.-',R='.-.',S='…',T='-',U='..-',V='…-',W='.--',X='-..-',Y='-.--',Z='--..')
frequency = 440
dot = 200
dash = 500

def play(word):
    for c in word:
        if c in morse.keys():
            m = morse[c]
            print("{0}:{1}".format(c,m))
            time.sleep(0.2)
            for i in m:
                if i == '.':
                    winsound.Beep(frequency,dot)
                else:
                    winsound.Beep(frequency,dash)
                time.sleep(0.1)
        else:
            print("{0} not in dictionary".format(c))
            
def main():
    try:
        print("Type only a-z, A-Z, or ctrl-c to exit")
        while True:
            word = input("Type a word: ")
            play(word.upper())
    except KeyboardInterrupt:
        print("ctrl-c command.")
    finally:
        print("Exiting program.")

if __name__ == "__main__":
    main()
