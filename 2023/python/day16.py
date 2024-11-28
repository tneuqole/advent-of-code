import functools
import itertools
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

start = datetime.now()

# python3 template.py < input
input = open(0).read().splitlines()

seen = [[False for i in range(len(input[0]))] for j in range(len(input))]
dirs = [[[] for i in range(len(input[0]))] for j in range(len(input))]


def go_left(x, y, grid):
    DIR = 4  # west
    count = 0
    if not seen[y][x]:
        count += 1
        seen[y][x] = True

    while True:
        x -= 1
        if x < 0:
            return count

        c = grid[y][x]
        if c == "." or c == "-":
            if not seen[y][x]:
                count += 1
                seen[y][x] = True
            continue

        if DIR in dirs[y][x]:
            return count

        dirs[y][x].append(DIR)

        if c == "/":
            dirs[y][x].append(DIR)
            return count + go_down(x, y, grid)
        elif c == "\\":
            return count + go_up(x, y, grid)
        elif c == "|":
            return count + go_up(x, y, grid) + go_down(x, y, grid)


def go_right(x, y, grid):
    DIR = 1  # east
    count = 0
    if not seen[y][x]:
        count += 1
        seen[y][x] = True

    while True:
        x += 1
        if x >= len(grid[y]):
            return count

        c = grid[y][x]
        if c == "." or c == "-":
            if not seen[y][x]:
                count += 1
                seen[y][x] = True
            continue

        if DIR in dirs[y][x]:
            return count

        dirs[y][x].append(DIR)

        if c == "/":
            return count + go_up(x, y, grid)
        elif c == "\\":
            return count + go_down(x, y, grid)
        elif c == "|":
            return count + go_up(x, y, grid) + go_down(x, y, grid)


def go_up(x, y, grid):
    DIR = 0  # north
    count = 0
    if not seen[y][x]:
        count += 1
        seen[y][x] = True

    while True:
        y -= 1
        if y < 0:
            return count

        c = grid[y][x]
        if c == "." or c == "|":
            if not seen[y][x]:
                count += 1
                seen[y][x] = True
            continue

        if DIR in dirs[y][x]:
            return count

        dirs[y][x].append(DIR)

        if c == "/":
            return count + go_right(x, y, grid)
        elif c == "\\":
            return count + go_left(x, y, grid)
        elif c == "-":
            return count + go_left(x, y, grid) + go_right(x, y, grid)
        elif c == "|":
            count += 1
            continue


def go_down(x, y, grid):
    DIR = 2  # south
    count = 0
    if not seen[y][x]:
        count += 1
        seen[y][x] = True

    while True:
        y += 1
        if y >= len(grid):
            return count

        c = grid[y][x]
        if c == "." or c == "|":
            if not seen[y][x]:
                count += 1
                seen[y][x] = True
            continue

        if DIR in dirs[y][x]:
            return count

        dirs[y][x].append(DIR)

        if c == "/":
            return count + go_left(x, y, grid)
        elif c == "\\":
            return count + go_right(x, y, grid)
        elif c == "-":
            return count + go_left(x, y, grid) + go_right(x, y, grid)


print(go_right(0, 0, input))

ans = 0
for i in range(len(input)):
    seen = [[False for i in range(len(input[0]))] for j in range(len(input))]
    dirs = [[[] for i in range(len(input[0]))] for j in range(len(input))]
    ans = max(ans, go_right(0, i, input))

    seen = [[False for i in range(len(input[0]))] for j in range(len(input))]
    dirs = [[[] for i in range(len(input[0]))] for j in range(len(input))]
    ans = max(ans, go_left(len(input[0]) - 1, i, input))


for i in range(len(input[0])):
    seen = [[False for i in range(len(input[0]))] for j in range(len(input))]
    dirs = [[[] for i in range(len(input[0]))] for j in range(len(input))]
    ans = max(ans, go_down(i, 0, input))

    seen = [[False for i in range(len(input[0]))] for j in range(len(input))]
    dirs = [[[] for i in range(len(input[0]))] for j in range(len(input))]
    ans = max(ans, go_up(i, len(input) - 1, input))

print(ans)
print(f"took={datetime.now() - start}")
