import urllib.request

def download_image(url):
    urllib.request.urlretrieve(url,"images/img.jpg")

url = input("Enter url: ")
download_image(url)
print("download successful")
