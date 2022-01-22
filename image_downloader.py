import urllib.request

import os

def download_image(url, path, name):
    save_path = str("data/" + name + ".jpg")
    #print(save_path)
    urllib.request.urlretrieve(url,save_path)
    print("cover download successful")


