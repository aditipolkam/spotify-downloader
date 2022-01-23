from email.mime import audio
import eyed3

def add_tags(file,title):
    audiofile = eyed3.load(str(file))
    if audiofile:
        audiofile.tag.title = title
        audiofile.tag.save()
        print("Tags embedded.")
    else:
        print("File not loaded")
    
