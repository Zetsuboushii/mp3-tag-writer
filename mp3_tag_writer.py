import os
import glob
import eyed3

for file in os.listdir("in/mp3"):
    if file.endswith(".mp3"):
        audiofile = eyed3.load(os.path.join("in/mp3", file))

        title_num = file.split("_")[0]
        title = file.split("_")[1].split(".")[0]
        if " -" in title:
            title = title.split(" -")[0]
        if title_num in title:
            title = title.replace(title_num + " ", "")
        title_num = file.split("_")[0].lstrip("0")

        with open("in/WRITE_ARTIST_NAME_IN_HERE", "r", encoding="utf-8") as artist_file:
            artist = artist_file.readline()
        with open("in/WRITE_ALBUM_NAME_IN_HERE", "r", encoding="utf-8") as album_file:
            album = album_file.readline()
        # with open(glob.glob("in/*.jpg")[0], "rb") as album_art_file:
        #     album_art = album_art_file.read()

        audiofile.tag.title = title
        audiofile.tag.artist = artist
        audiofile.tag.album = album
        audiofile.tag.track_num = title_num.lstrip("0")
        # audiofile.tag.images.set(3, album_art, "image/jpeg") #TODO shit doesnt work
        audiofile.tag.save()

        print("Title:", audiofile.tag.title)
        print("Artist:", audiofile.tag.artist)
        print("Album:", audiofile.tag.album)
        print("Track:", audiofile.tag.track_num[0])
        print("----------")
