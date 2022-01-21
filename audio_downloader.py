from pytube import YouTube

def download_audio(url, filename):
    yt = YouTube(url)
    stream = (yt.streams.filter(only_audio=True).last())
    stream.download(output_path = 'data/',filename = filename + ".mp3")
    print("audio download successful")