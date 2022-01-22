import eyed3

def add_tags(filename):
    audiofile = eyed3.load(str(filename))
    if audiofile:
        audiotag = eyed3.core.Tag(title="Trial",artist="Aditi",album="Trial",album_artist = "Various")
        audiofile.tag = audiotag
        audiofile.tag.save()
    else:
        print("File not loaded")

add_tags("data/trial.mp3",)
print("done")