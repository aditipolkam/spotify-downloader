import os
import pathlib
from dotenv import load_dotenv

from spotify import Spot
from image_downloader import download_image
from audio_downloader import download_audio
from youtube_search import search_song

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

if "data" not in os.listdir():
    os.mkdir("data")
temp_data_path = pathlib.Path("data")
output = pathlib.Path("data")

url = input("Enter url: ")
res = Spot(client_id=client_id, client_secret = client_secret).get_info(url)
#print(res)

for track in res['tracks']:
    #get data for track
    name = track['name']
    
    print("Starting download for: ", name)

    #search the song on ytmusicapi
    track_url = search_song(name)

    #download song audio
    audiofile = download_audio(track_url,name)

    

'''
    #download song cover image
    img_path = pathlib.Path(temp_data_path)
    #print(img_path)
    #download_image(album_cover_url,path,name)

    #converting the file to mp3
    convert_audio(audiofile, os.path.join(output,f"{name}.mp3"))


    #add tags to audio file
    #add_tags(f"data/{name}.mp3",)


'''
#song links to test
#https://open.spotify.com/track/0k5hoseEJnCAbpRh38dNoI?si=87f0453431d14f85
#https://open.spotify.com/track/3USxtqRwSYz57Ewm6wWRMp?si=99eb3680638d4189