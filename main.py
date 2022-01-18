import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

#lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
link = input("Enter url of the song:")

results = sp.track(link)
#print(results)
print("Track name: ",results['name'])
print("Artist: ", results['album']['artists'][0]['name'])
print("Release date: ", results['album']['release_date'])
#for track in results['tracks'][:10]:
   # print('track    :' + track['name'])



