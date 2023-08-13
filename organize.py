import os
import shutil

# Edit file extensions here
textExtensions = [".txt"]
imgExtensions = [".png", ".jpeg", ".jpg", ".gif", ".JPG", ".JPEG"]
audioExtensions = [".mp3"]
videoExtensions = [".mp4", ".webm", ".MP4"]
pdfExtensions = [".pdf"]
extraExtensions = [""] # you can add your own here

# Edir directory names here
textDirectoryName = "./Text/"
imgDirectoryName = "./Image/"
audioDirectoryName = "./Audio/"
videoDirectoryName = "./Video/"
pdfDirectoryName = "./Pdf/"
otherDirectoryName = "./Other/"
extraDirectoryName = "./dir/" #you can add your own here


def checkExtension(extension, list):
    if extension in list:
        return True
    return False


files = os.scandir()


for fl in files:
    if (os.path.isdir(fl.path)) or fl.name == "organize.py":
        print(fl.name + " is a directory")
        continue

    fileName = fl.name
    fileExtension = os.path.splitext(fl.name)[1]

    if checkExtension(fileExtension, textExtensions):  # check for texts
        print("Moving " + fileName)
        if not os.path.exists(textDirectoryName):
            os.mkdir(textDirectoryName)
        shutil.move(fileName, textDirectoryName + fileName)

    elif checkExtension(fileExtension, imgExtensions):  # check for images
        print("Moving " + fileName)
        if not os.path.exists(imgDirectoryName):
            os.mkdir(imgDirectoryName)
        shutil.move(fileName, imgDirectoryName + fileName)

    elif checkExtension(fileExtension, audioExtensions):  # check for audio
        print("Moving " + fileName)
        if not os.path.exists(audioDirectoryName):
            os.mkdir(audioDirectoryName)
        shutil.move(fileName, audioDirectoryName + fileName)

    elif checkExtension(fileExtension, videoExtensions):  # check for video
        print("Moving " + fileName)
        if not os.path.exists(videoDirectoryName):
            os.mkdir(videoDirectoryName)
        shutil.move(fileName, videoDirectoryName + fileName)

    elif checkExtension(fileExtension, pdfExtensions):  # check for pdf
        print("Moving " + fileName)
        if not os.path.exists(pdfDirectoryName):
            os.mkdir(pdfDirectoryName)
        shutil.move(fileName, pdfDirectoryName + fileName)
        
    elif checkExtension(fileExtension, extraExtensions):  # this is an example for if you need extra settings
        print("Moving " + fileName)
        if not os.path.exists(extraDirectoryName):
            os.mkdir(extraDirectoryName)
        shutil.move(fileName, extraDirectoryName + fileName) 

    else:
        print("Moving " + fileName + " into Other")
        if not os.path.exists(otherDirectoryName):
            os.mkdir(otherDirectoryName)
        shutil.move(fileName, otherDirectoryName + fileName)


print("Completed succesfully")
