import hashlib

string = "ckczppom"
start = 1

while True:
    puzzle = string + str(start)
    result = hashlib.md5(bytes(puzzle, 'utf-8'))
    digest = result.hexdigest()
    if digest[0:5] == "00000":
        print(digest)
        print(start)
    if digest[0:6] == "000000":
        print(digest)
        print(start)
        break
    start += 1
