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

# Edir directory names here
textDirectoryName = "./Text/"
imgDirectoryName = "./Image/"
audioDirectoryName = "./Audio/"
videoDirectoryName = "./Video/"
pdfDirectoryName = "./Pdf/"
otherDirectoryName = "./Other/"
```

if you need extra settings, just add another elif at the end:

``` python
yourNewDirectoryName = "./YourDir/"
youNewExtensionList = [".something", ".extension"]
elif checkExtension(fileExtension, yourNewDirectoryName):  
    print("Moving " + fileName)
    if not os.path.exists(yourNewDirectoryName):
        os.mkdir(yourNewDirectoryName)
    shutil.move(fileName, yourNewDirectoryName + fileName)

```