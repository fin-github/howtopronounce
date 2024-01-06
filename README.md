im too lazy to write docs
here are the args:

def create(word:str, ttspath:str = None, imgpath:str = None, check:bool = False):
    if ttspath is None: ttspath = f"tmp/{word}tts.mp3"
    if ttspath is None: imgpath = f"tmp/{word}img.mp3"


# check:
gives 0 if successful
1 if tts failed to save
2 if frame/img failed to save
