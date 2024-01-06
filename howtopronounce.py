from simplefuncs import *
from imgmaker import makeimg
from makevid import combine

def create(word:str, ttspath:str = None, imgpath:str = None, check:bool = False):
    if ttspath is None: ttspath = f"tmp/{word}tts.mp3"
    if ttspath is None: imgpath = f"tmp/{word}img.mp3"
    savetofile(word, ttspath)
    makeimg(word, imgpath)
    combine(imgpath, ttspath, word=word)
    if not check: return
    with open(ttspath, "r") as file:
        if file.read() == "": return 1
    with open(imgpath, "r") as file:
        if file.read() == "": return 2
    return 0