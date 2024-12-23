from datetime import datetime

start = datetime.now()

DIRS = {"<": (-1, 0), "^": (0, 1), ">": (1, 0), "v": (0, -1)}

data = open(0).read().strip()

seen = {(0, 0)}
x, y = 0, 0
for m in data:
    dx, dy = DIRS[m]
    x += dx
    y += dy
    seen.add((x, y))

print(len(seen))

seen = {(0, 0)}
x1, y1, x2, y2 = 0, 0, 0, 0
i = 0
while i < len(data):
    m = data[i]
    dx, dy = DIRS[m]
    x1 += dx
    y1 += dy
    seen.add((x1, y1))

    m = data[i + 1]
    dx, dy = DIRS[m]
    x2 += dx
    y2 += dy
    seen.add((x2, y2))

    i += 2

print(len(seen))

print(f"took={datetime.now() - start}")
