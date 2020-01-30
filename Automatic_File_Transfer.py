import os
import shutil

folder_to_track = "C:/Users/Krash/Downloads"
destinations = ( "/Texts", "/Images", "/Videos", "/Zips", "/Executables", "/Torrents", "/Files", "/Music" )
texts = (".txt", ".docx", ".pdf", ".doc" )
executables = ( ".exe", ".bat", ".apk" )
images = ( ".png", ".jpg", ".gif", ".jpeg" )
videos = ( ".wmv", ".mp4", ".mkv", ".flv", ".avi", ".amv" )
archives = ( ".zip", ".rar", ".jar" )
audio = ".mp3"
torrents = ".torrent"

i = 1
for filename in os.listdir(folder_to_track):
    new_name = filename

    folder_destination = "D:/My Downloads"
    if filename.endswith(texts):
        folder_destination += destinations[0]
    elif filename.endswith(images):
        folder_destination += destinations[1]
    elif filename.endswith(videos):
        folder_destination += destinations[2]
    elif filename.endswith(archives):
        folder_destination += destinations[3]
    elif filename.endswith(executables):
        folder_destination += destinations[4]
    elif filename.endswith(torrents):
        folder_destination += destinations[5]
    elif filename.endswith(audio):
        folder_destination += destinations[6]
    else:
        folder_destination += destinations[7]

    file_exists = os.path.isfile(folder_destination + "/" + new_name)
    while file_exists:
        i += 1
        name = os.path.splitext(new_name)[0]
        extention = os.path.splitext(new_name)[1]
        new_name = name + '(' + "{0}".format(i) + ')' + extention
        file_exists = os.path.isfile(new_name)

    src = folder_to_track + "/" + filename
    new_destination = folder_destination + "/" + new_name
    shutil.move(src, new_destination)