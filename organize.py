import os
import shutil

# Edit file extensions here
textExtensions = [".txt"]
imgExtensions = [".png", ".jpeg", ".jpg", ".gif", ".JPG", ".JPEG"]
audioExtensions = [".mp3"]
videoExtensions = [".mp4", ".webm", ".MP4"]
pdfExtensions = [".pdf"]
# you can add your own here
extraExtensions = ["", ""] 
extraExtensions0 = ["", ""]
extraExtensions1 = ["", ""]
extraExtensions2 = ["", ""]
extraExtensions3 = ["", ""]
extraExtensions4 = ["", ""]

# Edir directory names here
textDirectoryName = "./Text/"
imgDirectoryName = "./Image/"
audioDirectoryName = "./Audio/"
videoDirectoryName = "./Video/"
pdfDirectoryName = "./Pdf/"
otherDirectoryName = "./Other/"
 #you can add your own here
extraDirectoryName = "./dir/"
extraDirectoryName0 = "./dir/"
extraDirectoryName1 = "./dir/"
extraDirectoryName2 = "./dir/"
extraDirectoryName3 = "./dir/"
extraDirectoryName4 = "./dir/"


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

    if fileExtension == "": # moves files without extensions into other
        if not os.path.exists(otherDirectoryName):
            os.mkdir(otherDirectoryName)
        shutil.move(fileName, otherDirectoryName + fileName)
        
    elif checkExtension(fileExtension, textExtensions):  # check for texts
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
        
    elif checkExtension(fileExtension, extraExtensions0):  # this is an example for if you need extra settings
        print("Moving " + fileName)
        if not os.path.exists(extraDirectoryName0):
            os.mkdir(extraDirectoryName0)
        shutil.move(fileName, extraDirectoryName0 + fileName) 
        
    elif checkExtension(fileExtension, extraExtensions1):  # this is an example for if you need extra settings
        print("Moving " + fileName)
        if not os.path.exists(extraDirectoryName1):
            os.mkdir(extraDirectoryName1)
        shutil.move(fileName, extraDirectoryName1 + fileName) 
        
    elif checkExtension(fileExtension, extraExtensions2):  # this is an example for if you need extra settings
        print("Moving " + fileName)
        if not os.path.exists(extraDirectoryName2):
            os.mkdir(extraDirectoryName2)
        shutil.move(fileName, extraDirectoryName2 + fileName) 
        
    elif checkExtension(fileExtension, extraExtensions3):  # this is an example for if you need extra settings
        print("Moving " + fileName)
        if not os.path.exists(extraDirectoryName3):
            os.mkdir(extraDirectoryName3)
        shutil.move(fileName, extraDirectoryName3 + fileName) 
        
    elif checkExtension(fileExtension, extraExtensions4):  # this is an example for if you need extra settings
        print("Moving " + fileName)
        if not os.path.exists(extraDirectoryName4):
            os.mkdir(extraDirectoryName4)
        shutil.move(fileName, extraDirectoryName4 + fileName) 
        
    else:
        print("Moving " + fileName + " into Other")
        if not os.path.exists(otherDirectoryName):
            os.mkdir(otherDirectoryName)
        shutil.move(fileName, otherDirectoryName + fileName)


print("Completed succesfully")
