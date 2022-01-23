import urllib.request

import os
import pathlib
from pathlib import Path

def download_image(url, filepath, name):
    filename = str(name + ".jpg")
    img_path = Path(pathlib.Path(filepath, filename))
    urllib.request.urlretrieve(url,img_path)
    #print("cover download successful")
    return img_path


