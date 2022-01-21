import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spot:
    def __init__(self, client_id, client_secret):
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(auth_manager=auth_manager) 

    def get_info(self, link):
        #check what type of url
        l = link.split('/')

        if l[3] == "track":
            results = self.sp.track(link)
            artists = []
            for a in results['artists']:
                artists.append(a['name'])

            #track info
            track = {
                'id':results['id'],
                'name':results['name'],
                'release_date':results['album']['release_date'],
                'artist':artists,
                'album_name':results['album']['name'],
                'cover':results['album']['images'][0]['url'],
                'popularity':results['popularity'],
                'duration':"{:.2f}".format(results['duration_ms']/1000/60),
                'track_url':results['external_urls']['spotify'],
                'album_url':results['album']['external_urls']['spotify']
            }
            return track

        elif l[3] == "artist":
            results = self.sp.artist(link)
            artist_top_tracks = self.sp.artist_top_tracks(link)
            #print(artist_top_tracks)
            top_tracks = []

            for t in artist_top_tracks['tracks']:
                artists = []
                for a in t['artists']:
                    artists.append(a['name'])

                trackitem = {
                    'id':t['id'],
                    'name':t['name'],
                    'release_date':t['album']['release_date'],
                    'cover':t['album']['images'][0]['url'],
                    'artists':artists,
                    'url':t['external_urls']['spotify']
                }
                top_tracks.append(trackitem)

            artist = {
                'id':results['id'],
                'url':results['external_urls']['spotify'],
                'name':results['name'],
                'followers':results['followers']['total'],
                'genres':results['genres'],
                'cover':results['images'][0]['url'],
                'top_tracks':top_tracks
            }
            return artist

        elif l[3] == "album":
            results = self.sp.album(link)
            tracks = []
            album_artists = []
            for a in results['artists']:
                album_artists.append(a['name'])

            for t in results['tracks']['items']:
                #get all artists
                artists = []
                for a in t['artists']:
                    artists.append(a['name'])

                #get all genres

                trackitem = {
                    'name': t['name'],
                    'url': t['external_urls']['spotify'],
                    'artists':artists,
                }
                tracks.append(trackitem)

            album = {
                'name':results['name'],
                'genres':results['genres'],
                'popularity':results['popularity'],
                'release_date':results['release_date'],
                'total_tracks':results['total_tracks'],
                'url':results['external_urls']['spotify'],
                'cover':results['images'][0]['url'],
                'label':results['label'],
                'album_artists':album_artists,
                'tracks':tracks
            }
            return album

        elif l[3] == "playlist":
            results = self.sp.playlist(link)
            track_list = []

            for t in results['tracks']['items']:
                #get all artists
                artists = []
                for a in t['track']['artists']:
                    artists.append(a['name'])

                #details of each individual track
                trackitem = {
                    'id':t['track']['id'],
                    'name':t['track']['name'],
                    'album':t['track']['album']['name'],
                    'track_url':t['track']['external_urls']['spotify'],
                    'release_date':t['track']['album']['release_date'],
                    'artists':artists,
                    'album_cover':t['track']['album']['images'][0]['url'],
                    'album_url':t['track']['album']['external_urls']['spotify']
                }
                track_list.append(trackitem)

            #final dictionary of the playlist
            playlist = {
                'id': results['id'],
                'name': results['name'],
                'description': results['description'],
                'owner_name':results['owner']['display_name'],
                'total_tracks':results['tracks']['total'],
                'tracks':track_list
            }
            return playlist
        
    #print(results)
    #with open('results.txt','w') as FH:
        #    jsondata = json.dump(results,FH)