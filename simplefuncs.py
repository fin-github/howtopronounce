from pyttsx3 import init
from os import system as cmd
tts = init()

def clr(): cmd("cls")
def say(txt:str):
    tts.say(txt)
    tts.runAndWait()
def savetofile(txt:str, filename:str):
    tts.save_to_file(txt, filename=filename)
    tts.runAndWait()
