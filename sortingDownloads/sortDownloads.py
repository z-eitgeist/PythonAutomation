import os
import shutil

# Define source directory 
sourceDirectory = os.path.join(os.path.expanduser("~\Downloads"))

# Define destination directories
imagesDestDir = os.path.join(os.path.expanduser("~\Downloads"), "Download_Images")
videosDestDir = os.path.join(os.path.expanduser("~\Downloads"), "Download_Videos") 
musicDestDir = os.path.join(os.path.expanduser("~\Downloads"), "Download_Music")
documentDestDir = os.path.join(os.path.expanduser("~\Downloads"), "Download_Documents")
zipDestDir = os.path.join(os.path.expanduser("~\Downloads"), "Download_ZIP")

# If there is no destination directory, make one
if not os.path.exists(imagesDestDir):
    os.makedirs(imagesDestDir)
if not os.path.exists(videosDestDir):
    os.makedirs(videosDestDir)
if not os.path.exists(musicDestDir):
    os.makedirs(musicDestDir)
if not os.path.exists(documentDestDir):
    os.makedirs(documentDestDir)
if not os.path.exists(zipDestDir):
    os.makedirs(zipDestDir)

# Define supported extensions
image = [".png",".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".gif",
         ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
         ".jpf", ".jpx", ".jpm", ".jp2", ".j2k", ".jpf", ".heif", ".heic", 
         ".k25", ".bmp", ".dib", ".ind", ".indd", ".indt",  ".jpf", ".jpx",
         ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video = [".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov",".webm", ".mpg", 
         ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".avi", ".wmv", ".mov", 
         ".swf", ".qt", ".flv"]

audio = ["mp3", ".wav", ".m4a", ".flac", ".aac", ".wma"]

document = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"]

zip = [".zip", ".zipx", ".gzip", ".tar", ".rar", ".cab"]

# Define moving function
def moveFiles(destination, file):
    existingFile = os.path.join(sourceDirectory, file)
    shutil.move(existingFile, destination)

# get the list od all files in the Downloads folder
files = os.listdir(sourceDirectory)

# Sort files by extension to new directories
for file in files:
    if file.endswith(tuple(image)):
        destination = imagesDestDir
        moveFiles(destination, file)
    elif file.endswith(tuple(video)):
            destination = videosDestDir
            moveFiles(destination, file)
    elif file.endswith(tuple(audio)):
            destination = musicDestDir
            moveFiles(destination, file)
    elif file.endswith(tuple(document)):
            destination = documentDestDir
            moveFiles(destination, file)
    elif file.endswith(tuple(zip)):
            destination = zipDestDir
            moveFiles(destination, file)

print("Script completed.")
    
