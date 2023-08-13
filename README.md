# directory-sorter
A python directory sorter that will put all your files neatly into their respective folders according to their file extensions

## How to use

Place the organize.py file into the directory you want to sort and run this command

``` shell
python organize.py
```

## How to customise

You can modify the extensions and which files go where in first lines of the code:

``` python
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
```

if you need extra settings, just modify the extra settings. If you need even more, just copy and paste this code after an elif and edit the extraDirectoryName and extraExtensions variables.

``` python
    elif checkExtension(fileExtension, extraExtensions):
        if not os.path.exists(extraDirectoryName):
            os.mkdir(extraDirectoryName)
        shutil.move(fileName, extraDirectoryName + fileName) 
```