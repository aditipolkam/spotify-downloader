import urllib.request

def download_image(url):
    urllib.request.urlretrieve(url,"images/img.jpg")
    print("download successful")


