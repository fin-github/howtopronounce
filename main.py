try:
    import pyttsx3
    from sys import argv
    from os import system as cmd
    from simplefuncs import *
    from imgmaker import makeimg
    from makevid import combine
except ModuleNotFoundError:
    quit(1212)

tts = pyttsx3.init()
args = argv
args.pop(0)

try:
    word = args[0]
except IndexError:
    word = input("Please enter a word: ")
print(f"Running with {word}")


# main thing
savetofile(word, "tmp/word.mp3")
makeimg(word, "tmp/img.png")
combine("tmp/img.png", "tmp/word.mp3", word=word)
