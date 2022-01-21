import os
from platform import release
from dotenv import load_dotenv

from spotify import Spot
from image_downloader import download_image
from audio_downloader import download_audio
from youtube_search import search_song
#from song_tags import add_tags

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

url = input("Enter url: ")
res = Spot(client_id=client_id, client_secret = client_secret).get_info(url)
#print(res)

for track in res['tracks']:
    #get data for track
    name = track['name']
    album_cover_url = track['album_cover']
    album = track['album']
    artists = track['artists']
    release_date = track['release_date']

    print("Starting download for: ", name)
    #download song cover image
    download_image(album_cover_url,name)

    #search the song on ytmusicapi
    track_url = search_song(name)

    #download song audio
    download_audio(track_url,name)

    #add tags to audio file
    #add_tags(f"data/{name}.mp3",)
