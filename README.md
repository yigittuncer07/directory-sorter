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
# you can add your own here
extraExtensions = ["", ""] 
extraExtensions0 = ["", ""]
extraExtensions1 = ["", ""]
extraExtensions2 = ["", ""]
extraExtensions3 = ["", ""]
extraExtensions4 = ["", ""]


# Edit directory names here
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
```

if you need extra settings, just modify the extra variables. If you need even more, you can copy and paste this before the else in line 122. Be sure to modify the extra variables.
``` python
elif checkExtension(fileExtension, extraExtensions5):
    print("Moving " + fileName)
    if not os.path.exists(extraDirectoryName5):
            os.mkdir(extraDirectoryName5)
    shutil.move(fileName, extraDirectoryName5 + fileName) 
        
```

# To-Do
- Read directories and extensions from a file
- Get path of directory to be sorted from user
