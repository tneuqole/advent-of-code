import functools
from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

W, H = 101, 103
mw, mh = W // 2 - 1, H // 2 - 1
coords = defaultdict(int)
robots = []
for row in data:
    parts = row.split(" ")
    x = int(parts[0].split(",")[0][2:])
    y = int(parts[0].split(",")[1])
    vx = int(parts[1].split(",")[0][2:])
    vy = int(parts[1].split(",")[1])

    robots.append((x, y, vx, vy))

    newx = (vx * 100 + x) % W
    newy = (vy * 100 + y) % H

    if newx <= mw and newy <= mh:
        coords[0] += 1
    elif newx >= mw + 2 and newy <= mh:
        coords[1] += 1
    elif newx <= mw and newy >= mh + 2:
        coords[2] += 1
    elif newx >= mw + 2 and newy >= mh + 2:
        coords[3] += 1

print(functools.reduce(lambda a, b: a * b, coords.values()))

i = 0
while True:
    i += 1
    seen = set()
    grid = [[" " for _ in range(W)] for _ in range(H)]

    for x, y, vx, vy in robots:
        newx = (vx * i + x) % W
        newy = (vy * i + y) % H
        seen.add((newx, newy))
        grid[newy][newx] = "."

    if len(seen) == len(robots):
        print(i)
        for row in grid:
            print("".join(row))  # merry christmas

        break


print(f"took={datetime.now() - start}")
