import sys
from ytmusicapi import YTMusic

def search_song(name):
    ytm = YTMusic()
    result = ytm.search(name, filter="songs")
    try:
        videoid = result[0]["videoId"]
    except KeyError or IndexError:
        videoid=""
        print("Song not found.")
        sys.exit()

    video_url = "https://www.youtube.com/watch?v="+videoid
    return video_url

