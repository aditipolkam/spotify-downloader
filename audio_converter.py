from fileinput import filename
from importlib.resources import path
import ffmpeg 
import os
import pathlib

def convert_audio(inputfile,outputfile):
    inputfile = ffmpeg.input(inputfile)
    if inputfile:
        audiofile = inputfile.audio
        #os.remove('data/Heat Waves.mp3')

        out = ffmpeg.output(audiofile,str(pathlib.Path(outputfile)), format="mp3") 
        ffmpeg.run(out)
    else:
        print("file not loaded.")
