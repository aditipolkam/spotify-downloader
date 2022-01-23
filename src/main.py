import os
import pathlib
from typing import final
from dotenv import load_dotenv
from numpy import save

from spotify import Spot
from image_downloader import download_image
from audio_downloader import download_audio
from youtube_search import search_song
from audio_converter import convert_audio
from song_tags import add_tags

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

if "downloads" not in os.listdir():
    os.mkdir("downloads")

save_path = './downloads/'

url = input("Enter url: ")
res = Spot(client_id=client_id, client_secret = client_secret).get_info(url)
#print(res)

for track in res['tracks']:
    #get data for track
    name = track['name']
    album_cover_url = track['album_cover']
    
    print("Starting download for: ", name)

    #search the song on ytmusicapi
    track_url = search_song(name)

    #download song audio
    audiofile = download_audio(track_url,name,save_path)

    
    #download song cover image
    img_path = pathlib.Path(save_path)
    print(img_path)
    #cover_img = download_image(album_cover_url,img_path,name)

    #converting the file to mp3
    convert_audio(audiofile, os.path.join(save_path,f"{name}.mp3"))

    #add tags to audio file
    final_path = os.path.join(save_path,f"{name}.mp3")
    add_tags(final_path, name)



#song links to test
#https://open.spotify.com/track/0k5hoseEJnCAbpRh38dNoI?si=87f0453431d14f85
#https://open.spotify.com/track/3USxtqRwSYz57Ewm6wWRMp?si=99eb3680638d4189