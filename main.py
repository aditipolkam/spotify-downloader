import os
from dotenv import load_dotenv

from spotify import Spot
from image_downloader import download_image
from audio_downloader import download_audio


load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

url = input("Enter url: ")
res = Spot(client_id=client_id, client_secret = client_secret).get_info(url)
#print(res)

album_cover_url = res["cover"]
name = res["name"]

#download song cover image
download_image(album_cover_url,name)

#download song audio
track_url = input("Enter track url:")
download_audio(track_url,name)


