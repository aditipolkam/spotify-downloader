from fileinput import filename
from importlib.resources import path
import ffmpeg 
import os
import pathlib

def convert_audio(file_path, outputfile):
    inputfile = ffmpeg.input(file_path)
    if inputfile:
        audiofile = inputfile.audio
        out = ffmpeg.output(audiofile,str(pathlib.Path(outputfile)), format="mp3") 
        ffmpeg.run(out)
        os.remove(file_path)
    else:
        print("file not loaded.")
