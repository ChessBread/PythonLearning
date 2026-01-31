# (.txt , .json, .csv)
import csv

file_path  = "/home/aldie/Documents/alden.py/WriteFiles/pizza.txt"

try:
    with open(file_path,"r")  as file:
        content = file.read()
        #content = json.load(file)
        # print(content["age"])
        print(content)

        #content  = csv.reader(file)
        #for line in content:
            #print(line[0])

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("you do not have permission to read that file")