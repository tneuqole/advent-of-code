import functools
import itertools
from collections import defaultdict, deque
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

start = datetime.now()

input = open(0).read().splitlines()


def get_coords(line):
    c = [(0, 0)]
    for p in line.split(","):
        x, y = c[-1]

        dir, dist = p[0], int(p[1:])

        if dir == "U":
            y += dist
        elif dir == "D":
            y -= dist
        elif dir == "L":
            x -= dist
        elif dir == "R":
            x += dist

        c.append((x, y))

    return c


c1 = get_coords(input[0])
c2 = get_coords(input[1])

i = 0
intersections = set()

for i in range(len(c1) - 1):
    x1, y1 = c1[i]
    x2, y2 = c1[i + 1]

    line1 = {}
    if x1 != x2:
        line1 = {(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)}
    else:
        assert y1 != y2
        line1 = {(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)}

    for j in range(len(c2) - 1):
        x3, y3 = c2[j]
        x4, y4 = c2[j + 1]

        line2 = {}
        if x3 != x4:
            line2 = {(x, y3) for x in range(min(x3, x4), max(x3, x4) + 1)}
        else:
            line2 = {(x3, y) for y in range(min(y3, y4), max(y3, y4) + 1)}

        intersections.update(line1 & line2)


intersections.remove((0, 0))
print(f"p1={min(abs(x) + abs(y) for x, y in intersections)}")


total_steps = defaultdict(list)


def count_steps(coords):
    steps = 0
    for i in range(len(coords) - 1):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]

        line = {}
        if x1 != x2:
            line = {(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)}
            inter = line & intersections
            if inter:
                for x, y in inter:
                    # inter_steps = steps + max(abs(x1), abs(x)) - min(abs(x1), abs(x))
                    inter_steps = steps + max(x1, x) - min(x1, x)
                    total_steps[(x, y)].append(inter_steps)

            steps += max(x1, x2) - min(x1, x2)
        else:
            assert y1 != y2
            line = {(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)}
            inter = line & intersections
            if inter:
                for x, y in inter:
                    # inter_steps = steps + max(abs(y1), abs(y)) - min(abs(y1), abs(y))
                    inter_steps = steps + max(y1, y) - min(y1, y)
                    total_steps[(x, y)].append(inter_steps)

            steps += max(y1, y2) - min(y1, y2)

    return total_steps


count_steps(c1)
count_steps(c2)

print(min(sum(v) for v in total_steps.values()))

print(f"took={datetime.now() - start}")
