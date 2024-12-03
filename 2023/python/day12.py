import functools
from datetime import datetime

from input import *


@functools.cache
def calc(record, groups) -> int:
    if not groups:
        if "#" not in record:
            return 1
        return 0

    if not record:
        return 0

    c = record[0]
    g = groups[0]

    if c == ".":
        return calc(record[1:], groups)
    elif c == "#":
        s = record[:g]
        s = s.replace("?", "#")

        if s != g * "#" or (g < len(record) and record[g] == "#"):
            return 0

        if g < len(record) and record[g] == "?":
            return calc(record[g + 1 :], groups[1:])

        return calc(record[g:], groups[1:])

    # treat ? as both # and .
    return calc("#" + record[1:], groups) + calc("." + record[1:], groups)


ans = 0
start = datetime.now()
for line in input.splitlines():
    if not line:
        continue

    data = line.split(" ")

    # p1
    # record = data[0]
    # groups = [int(i) for i in data[1].split(",")]

    # p2
    record = ((data[0] + "?") * 5)[:-1]
    groups = [int(i) for i in data[1].split(",")] * 5

    ans += calc(record, tuple(groups))

print(ans)
print(f"took={datetime.now() - start}")
