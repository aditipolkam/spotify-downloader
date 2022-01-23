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
            artists = ""
            for a in results['artists']:
                artists = artists + f"{a['name']} "

            #track info
            tracklist = [{
                'track_name':results['name'],
                'release_date':results['album']['release_date'],
                'artists':artists,
                'album_name':results['album']['name'],
                'album_cover':results['album']['images'][0]['url']
            }]

            track = {
                'tracks': tracklist
            }
            return track

        elif l[3] == "artist":
            results = self.sp.artist(link)
            artist_top_tracks = self.sp.artist_top_tracks(link)
            #print(artist_top_tracks)
            top_tracks = []

            for t in artist_top_tracks['tracks']:
                artists = ""
                for a in t['artists']:
                    artists = artists + f"{a['name']} "

                trackitem = {
                    'track_name':t['name'],
                    'release_date':t['album']['release_date'],
                    'album_name':t['album']['name'],
                    'album_cover':t['album']['images'][0]['url'],
                    'artists':artists
                }
                top_tracks.append(trackitem)

            artist = {
                'name':results['name'],
                'followers':results['followers']['total'],
                'genres':results['genres'],
                'tracks':top_tracks
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
                artists = ""
                for a in t['artists']:
                    artists = artists + f"{a['name']} "

                trackitem = {
                    'track_name':t['name'],
                    'release_date':results['release_date'],
                    'album_name':results['name'],
                    'album_cover':results['images'][0]['url'],
                    'artists':artists
                }
                tracks.append(trackitem)

            album = {
                'name':results['name'],
                'release_date':results['release_date'],
                'total_tracks':results['total_tracks'],
                'album_cover':results['images'][0]['url'],
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
                artists = ""
                for a in t['track']['artists']:
                    artists = artists + f"{a['name']} "

                #details of each individual track
                trackitem = {
                    'track_name':t['track']['name'],
                    'album_name':t['track']['album']['name'],
                    'release_date':t['track']['album']['release_date'],
                    'artists':artists,
                    'album_cover':t['track']['album']['images'][0]['url']
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
        
 