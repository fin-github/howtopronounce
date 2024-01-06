from simplefuncs import *
from imgmaker import makeimg
from makevid import combine

def create(word:str, ttspath:str = None, imgpath:str = None, check:bool = False):
    if ttspath is None: fixedttspath = f"tmp/{word}tts.mp3"
    else: fixedttspath = ttspath
    if ttspath is None: fixedimgpath = f"tmp/{word}img.png"
    else: fixedimgpath = imgpath
    savetofile(word, fixedttspath)
    makeimg(word, fixedimgpath)
    combine(fixedimgpath, fixedttspath, word=word)
    if not check: return
    with open(ttspath, "r") as file:
        if file.read() == "": return 1
    with open(imgpath, "r") as file:
        if file.read() == "": return 2
    return 0
