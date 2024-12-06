import sys
import requests
import os
from datetime import date
import browser_cookie3
import shutil

### WRITEN BY antooro - https://github.com/antooro/advent-of-code-2019/blob/master/startDay.py

# Get cookies from the browser
cj = browser_cookie3.firefox()
if not (".adventofcode.com" in str(cj)):
    cj = browser_cookie3.chrome()

# Get today number of day
day_today = date.today().strftime("%d").lstrip("0")

# If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if day < 0 or day > 31:
        exit("Day is not valid")
else:
    day = day_today

print(f"Initializing day {day}")

if not os.path.exists(f"day{day}"):
    shutil.copytree("Template", f"day{day}")
    os.chdir(f"day{day}")

    r = requests.get(f"https://adventofcode.com/2024/day/{day}/input", cookies=cj)

    with open(f"input.txt", "w") as f:
        f.write(r.text)
