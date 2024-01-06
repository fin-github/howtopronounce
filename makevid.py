from moviepy.editor import ImageSequenceClip, AudioFileClip

def combine(imgname:str, audioname:str, word:str):
    # Replace this list with the file names of your images
    image_files = [imgname]

    # Create an ImageSequenceClip from the list of images
    video_clip = ImageSequenceClip(image_files, fps=24)
    
    audio = AudioFileClip(audioname)
    
    video_clip = video_clip.set_audio(audio)

    # Write the video to a file
    video_clip.write_videofile(f"results/{word}.mp4", codec="libx264", audio_codec="aac")
