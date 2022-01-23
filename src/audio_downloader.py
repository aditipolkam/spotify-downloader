from pytube import YouTube
import pathlib

def download_audio(url, filename,save_path):
    path = pathlib.Path(save_path)
    yt = YouTube(url)
    stream = (yt.streams.filter(only_audio=True).last())
    outfile = stream.download(output_path = path ,filename = filename)
    #print("audio download successful")
    #print(outfile)
    return outfile