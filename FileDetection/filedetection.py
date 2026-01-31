#file dectection

import os

file_path = "/home/aldie/Documents/alden.py/FileDetection/studd"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")


    if os.path.isfile(file_path):
        print("That is a file")

    elif os.path.isdir(file_path):
        print("This is a folder")

else:
    print(f"'{file_path}' cant be found")