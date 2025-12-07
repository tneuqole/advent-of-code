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

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

data = list(map(list, open(0).read().strip().splitlines()))

ans1 = 0
beams = {70}
for y in range(1, len(data)):
    new_beams = set()
    for beam in beams:
        if data[y][beam] == ".":
            new_beams.add(beam)
            continue

        ans1 += 1

        if beam > 0:
            new_beams.add(beam - 1)
        if beam < len(data[0]) - 1:
            new_beams.add(beam + 1)

    beams = new_beams

print(f"ans1= {ans1}")

MAX = len(data[0]) - 1

beams = defaultdict(int)
beams[(0, 70)] = 1
for next_y in range(1, len(data)):
    coords = list(beams.keys())
    new_beams = defaultdict(int)

    for y, x in coords:
        if data[next_y][x] == ".":
            new_beams[(next_y, x)] += beams[(y, x)]
            continue

        if x > 0:
            new_beams[(next_y, x - 1)] += beams[(y, x)]
        if x < MAX:
            new_beams[(next_y, x + 1)] += beams[(y, x)]

    beams = new_beams


print(f"ans2= {sum(beams.values())}")


print(f"took={datetime.now() - start}")
