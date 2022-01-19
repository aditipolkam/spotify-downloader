import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_info(link):
    l = link.split('/')

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
        track_list = []

        for t in results['tracks']['items']:

            #get all artists
            artists = []
            for a in t['track']['artists']:
                artists.append(a['name'])

            #details of each individual track
            trackitem = {}
            trackitem['name'] = t['track']['name']
            trackitem['album'] = t['track']['album']['name']
            trackitem['release_date']=t['track']['album']['release_date']
            trackitem['artists'] = artists
            trackitem['album_cover'] = t['track']['album']['images'][0]['url']
            trackitem['album_url'] = t['track']['album']['external_urls']['spotify']
            track_list.append(trackitem)

        #final dictionary of the playlist
        playlist = {
            'name': results['name'],
            'description': results['description'],
            'owner_name':results['owner']['display_name'],
            'total_tracks':results['tracks']['total'],
            'tracks':track_list
        }
        return playlist



link = input("Enter url:")
info = get_info(link)
print(info)
    
#print(results)
 #with open('results.txt','w') as FH:
    #    jsondata = json.dump(results,FH)