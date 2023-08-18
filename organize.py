import os
import shutil


extensions_and_directories = []
other_directory = "Other"


def read_config_file():
    lines = get_lines("config.txt")
    line = " "
    directory_name = ""
    for line in lines:
        file_extensions_list = []
        words = line.split()
        for j in range(len(words) - 1):
            file_extensions_list.append(words[j])
        directory_name = words[len(words) - 1]
        extensions_and_directories.append([file_extensions_list, directory_name])


def get_lines(file_name: str) -> [str]:
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines


def extension_in_list(extension, list):
    if extension in list:
        return True
    return False


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1][1:]


def move_file(file_name, directory_name):
    if not os.path.exists(directory_name):
        print("creating directory " + directory_name)
        os.mkdir(directory_name)
    print("moving " + file_name + " into " + directory_name)
    shutil.move(file_name, directory_name + "/" + file_name)


read_config_file()
files = os.scandir()
print(extensions_and_directories)


for fl in files:
    # Does not move program files and directories
    if (
        os.path.isdir(fl.path)
        or fl.name == "organize.py"
        or fl.name == "config.txt"
        or fl.name[0] == "."
    ):
        continue

    file_name = fl.name
    file_extension = get_file_extension(file_name)

    # Loops through extensions to find fit
    for ex_dir in extensions_and_directories:
        extensions = ex_dir[0]
        directory_name = ex_dir[1]
        if extension_in_list(file_extension, extensions):
            move_file(file_name,directory_name)

    # If no fit is found, move into other
    if (os.path.exists(file_name)):
        move_file(file_name,"Other")
        


print("Completed succesfully")
