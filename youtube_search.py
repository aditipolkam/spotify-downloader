from ytmusicapi import YTMusic

def search_song(name):
    ytm = YTMusic()
    result = ytm.search(name, filter="songs")
    videoid = result[0]["videoId"]
    video_url = "https://www.youtube.com/watch?v="+videoid
    return video_url

