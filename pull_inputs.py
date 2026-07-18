import os

with open("cookie") as file:
    SESSION_COOKIE = file.read()

if not SESSION_COOKIE:
    exit()

YEARS = [2026] # year or years you cant to pull for
DAYS = 12 # day you want to pull up to

for year in YEARS:
    for day in range(1, DAYS + 1):

        # Ensure the directory exists first
        os.makedirs(f"{year}/data", exist_ok=True)

        # Prepend a 0 onto days 1->9 so they are 01, 02, etc
        day_string = str(day)
        if day < 10:
            day_string = "0" + str(day)

        # Build the command
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        output_file = f"{year}/data/day{day_string}.txt"

        # Execute!
        os.system(f"curl {url} -H \"cookie: session={SESSION_COOKIE}\" -o {output_file}")
