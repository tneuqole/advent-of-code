import re
from datetime import datetime

start = datetime.now()

input = open(0).read()

matches = re.findall(r"mul\(\d+,\d+\)", input)
print(sum(int(m.split(",")[0][4:]) * int(m.split(",")[1][:-1]) for m in matches))

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
do = True
sum = 0
for m in matches:
    if m == "do()":
        do = True
    elif m == "don't()":
        do = False
    elif do:
        sum += int(m.split(",")[0][4:]) * int(m.split(",")[1][:-1])

print(sum)

print(f"took={datetime.now() - start}")
