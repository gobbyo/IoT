import time
import winsound

morse = dict(A='.-',B='-...',C='-.-.',D='-..',E='.',F='..-.',G='--.',H='....',I='..',J='.---',K='-.-',L='.-..',M='--',N='-.',O='---',P='.--.',Q='--.-',R='.-.',S='...',T='-',U='..-',V='...-',W='.--',X='-..-',Y='-.--',Z='--..')
frequency = 440
dotlength = 150
dashlength = 500
wordpause = 1
letterpause = 0.3
morsepause = 0.15

def play(word):
    for c in word:
        if c in morse.keys():
            m = morse[c]
            print("{0}:{1}".format(c,m))
            for i in m:
                if i == '.':
                    winsound.Beep(frequency,dotlength)
                else:
                    winsound.Beep(frequency,dashlength)
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
        print("Exiting program.")

if __name__ == "__main__":
    main()
