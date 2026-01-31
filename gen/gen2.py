def read_file(file_path):
    with open(file_path)  as file:
        for line in file:
            yield line.strip()


file_path  = "/home/aldie/Documents/alden_python/gen/hit.txt"

for line  in read_file(file_path):
    print(line)