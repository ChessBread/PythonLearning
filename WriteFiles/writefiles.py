# (.txt , .json. .csv)

import json
import csv

employees = [ ["name", "age", "job"],
              ["spongebob", "30", "cook"], 
              ["Patric", 37, "Unemployed"], 
              ["Sandy", 27, "scientist"]]

file_path = "/home/aldie/Documents/alden.py/WriteFiles/pizza.csv"


try:
    with open(file_path, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)

        print(f"csv file {file_path} was created")
except FileExistsError:
    print("this file already exists")
