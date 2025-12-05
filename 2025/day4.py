import functools
import heapq
import itertools
import math
import re
from collections import defaultdict, deque
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

start = datetime.now()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

raw = open(0).read().strip().splitlines()

data = []
for row in raw:
    data.append(list(row))


def count(data):
    coords = []
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == ".":
                continue

            adj = 0
            for dy, dx in DIRS:
                ny, nx = y + dy, x + dx
                if ny >= 0 and ny < len(data) and nx >= 0 and nx < len(data[y]):
                    adj += 1 if data[ny][nx] == "@" else 0

            if adj < 4:
                coords.append((y, x))

    return coords


ans1 = len(count(data))

print(f"ans1= {ans1}")

ans2 = 0
while True:
    coords = count(data)
    if len(coords) == 0:
        break
    ans2 += len(coords)
    for y, x in coords:
        data[y][x] = "."

print(f"ans2= {ans2}")

print(f"took={datetime.now() - start}")
