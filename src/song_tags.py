import eyed3
import os

def add_tags(file, title, album_name, release_date, artists, cover_img):
    audiofile = eyed3.load(str(file))
    if audiofile:
        audiofile.tag.title = title
        audiofile.tag.album = album_name
        audiofile.tag.artist = artists
        audiofile.tag.release_date = release_date
        with open(cover_img, "rb") as cover_art:
            audiofile.tag.images.set(3, cover_art.read(), "image/jpeg")

        
        audiofile.tag.save(version=(1, None, None))
        audiofile.tag.save(version = (2,3,0))
        audiofile.tag.save()

        #remove cover img i.e. not required
        os.remove(cover_img)
        print("Tags embedded.")
    else:
        print("File not loaded")
    
