# Galaxy brain idea..

# First, we read the file, and convert it into valid shell code

with open("data/day07.txt") as file:
    history = file.read().splitlines()[1:]

shell_code = f"cd day07_tree/\n"

for c in history:
    if c == "$ ls": continue
    elif c[0] == 'd': shell_code += f"mkdir {c[4:]}\n"
    elif c[0] == '$': shell_code += f"{c[2:]}\n"
    else:
        size, name = c.split()
        shell_code += f"fallocate -l {int(size)} {name}\n"

# Then run the output to make the tree in your filesystem

import os

os.system("mkdir day07_tree")
os.system(shell_code)

# Now, call `tree` and output the structure as a JSON object
os.system(f"tree -s -J day07_tree/ > data/day07_tree.json")

# Roundabout I know, but I really dislike this data type

import json

# Then, read that JSON, and do stuff!

with open(f"data/day07_tree.json") as file:
    tree = json.loads(file.read())[0]["contents"]

def get_dir_size(tree):
    dir_size = 0
    for attr in tree:
        if attr["type"] == "file":
            dir_size += attr["size"]
        if attr["type"] == "directory":
            size = get_dir_size(attr["contents"])
            attr["size"] = size
            dir_size += size
    return dir_size

size = get_dir_size(tree)

def get_dirs_under(size, tree):
    dirs = []
    for attr in tree:
        if attr["type"] == "directory":
            if attr["size"] <= size:
                dirs.append(attr["size"])
            dirs += get_dirs_under(size, attr["contents"])
    return dirs

def get_dirs_over(size, tree):
    dirs = []
    for attr in tree:
        if attr["type"] == "directory":
            if attr["size"] >= size:
                dirs.append(attr["size"])
            dirs += get_dirs_over(size, attr["contents"])
    return dirs

dirs_1 = get_dirs_under(100000, tree)
dirs_2 = get_dirs_over(30000000 - (70000000 - size), tree)

print(f"Part one = {sum(dirs_1)}")
print(f"Part two = {min(dirs_2)}")

# Housekeeping!

os.system("rm -r day07_tree")
os.system("rm data/day07_tree.json")