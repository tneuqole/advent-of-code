from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

DIRS = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "3": (-1, 0),
    "0": (0, 1),
    "1": (1, 0),
    "2": (0, -1),
}


def shoelace(p):
    area = 0
    for i in range(len(p) - 1):
        area += (p[i][0] * p[i + 1][1]) - (p[i + 1][0] * p[i][1])

    return abs(int(area / 2))


def picks(area, p_len):
    return int(area + 1 - p_len / 2)


def parse_hex(h):
    return DIRS[h[-2]], int(h[2:-2], 16)


r1, c1 = 0, 0
r2, c2 = 0, 0
perimeter1 = [(0, 0)]
perimeter2 = [(0, 0)]
for row in data:
    parts = row.split(" ")
    dr, dc = DIRS[parts[0]]
    for _ in range(int(parts[1])):
        r1 += dr
        c1 += dc
        perimeter1.append((r1, c1))

    d, count = parse_hex(parts[2])
    dr, dc = d
    for _ in range(count):
        r2 += dr
        c2 += dc
        perimeter2.append((r2, c2))


area = shoelace(perimeter1)
p_len = len(perimeter1)
print(p_len + picks(area, p_len))

area = shoelace(perimeter2)
p_len = len(perimeter2)
print(p_len + picks(area, p_len))


print(f"took={datetime.now() - start}")
