file_path = "/home/aldie/Documents/alden_python/gen/hit.txt"

with open(file_path) as file:
    lines = (line.strip() for line in file)
    for line in  lines:
        print(line)