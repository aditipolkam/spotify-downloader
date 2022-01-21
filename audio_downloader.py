from pytube import YouTube

def download_audio(url, filename):
    yt = YouTube(url)
    print(url)
    print(yt.title)
    print(yt.thumbnail_url)
    print(yt.streams)
    stream = (yt.streams.filter(only_audio=True).last())
    stream.download(output_path = 'audios/',filename = filename + ".mp3")

video_url = input("Enter url: ")
filename = input("Enter filename: ")
download_audio(video_url, filename)