import os
from dotenv import load_dotenv

from spotify import Spot
from image_downloader import download_image

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

url = input("Enter url: ")
res = Spot(client_id=client_id, client_secret = client_secret).get_info(url)
#print(res)

album_cover = res["cover"]
download_image(album_cover)

