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
link = input("Enter url:")

l = link.split('/')
#print(l)

if l[3] == "track":
    results = sp.track(link)
    track = {
        'name':results['name'],
        'release_date':results['album']['release_date'],
        'artist':results['album']['artists'],
        'album_type':results['album']['album_type'],
        'images':results['album']['images'],
        'popularity':results['popularity'],
        'duration':"{:.2f}".format(results['duration_ms']/1000/60)
    }
    print(track)

elif l[3] == "artist":
    results = sp.artist(link)
    #print(results)
    artist = {
        'id':results['id'],
        'name':results['name'],
        'followers':results['followers']['total'],
        'genres':results['genres']
    }
    print(artist)

elif l[3] == "album":
    results = sp.album(link)
    album = {
        'name':results['name'],
        'genres':results['genres'],
        "popularity":results['popularity'],
        "release_date":results['release_date'],
        "total_tracks":results['total_tracks'],
        'tracks':results['tracks']
    }
    print(album)

elif l[3] == "playlist":
    results = sp.playlist(link)
    playlist = {
        'name': results['name'],
        'description': results['description'],
        'owner_name':results['owner']['display_name'],
        'tracks':results['tracks']['items']
    }
    print(playlist)
#print(results)