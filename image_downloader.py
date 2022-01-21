import urllib.request

def download_image(url, name):
    urllib.request.urlretrieve(url,str("data/" + name + ".jpg"))
    print("cover download successful")


