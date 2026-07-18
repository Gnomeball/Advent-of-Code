def process_disk():
    with open("data/day09.txt") as file:
        disk = list(map(int, [ _ for _ in file.read()]))

    disk_map = []
    file_len = []     # (size, start)
    free_len = []     # (size, start)

    current_id = -1
    free_space = False

    for f in disk:
        count = int(f)
        if free_space:
            block_id = -1   # -1 is free space
            free_len.append((count, len(disk_map)))
        else:
            current_id += 1
            block_id = f
            file_len.append((count, len(disk_map)))
        for n in range(count):
            disk_map.append(block_id if free_space else current_id)
        free_space = not free_space

    return disk_map, file_len, free_len

disk_map, file_len, free_len = process_disk()

# Part one: Function to re-order the files on a disk

def reorder_disk(disk):
    while -1 in disk:
        f = disk.pop(len(disk) -1)
        disk[disk.index(-1)] = f
    return disk

reordered_disk = reorder_disk(disk_map.copy())

# Function to calculate the check sum of a file map

def checksum(disk):
    return sum(i * int(f) for i,f in enumerate(disk) if f >= 0)

print(f"Part one: {checksum(reordered_disk)}")

# Part two: Function to compact files on a disk

def compact(disk_map, file_len, free_len):
    for b_id in reversed(range(len(file_len))):
        b_len, b_pos = file_len[b_id]
        for f, (f_len, f_pos) in enumerate(free_len):
            if f_pos > b_pos:
                break # we don't want to move files to right
            if f_len >= b_len:
                for pos in range(f_pos, f_pos + b_len):
                    disk_map[pos] = b_id # move block to free space
                for pos in range(b_pos, b_pos + b_len):
                    disk_map[pos] = -1  # mark old block as free
                free_len[f] = (f_len - b_len, f_pos + b_len)
                break
    return disk_map

compacted_disk = compact(disk_map, file_len, free_len)

print(f"Part two: {checksum(compacted_disk)}")
