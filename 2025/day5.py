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

data = open(0).read().strip().splitlines()

idx = 0
ranges = []
ids = []
while idx < len(data):
    if data[idx] == "":
        break

    ranges.append(tuple(map(int, data[idx].split("-"))))
    idx += 1

idx += 1
while idx < len(data):
    ids.append(int(data[idx]))
    idx += 1


ans1 = set()
for x, y in ranges:
    for id in ids:
        if x <= id and id <= y:
            ans1.add(id)

print(f"ans1= {len(ans1)}")


def cycle(ranges):
    cur = deepcopy(ranges)
    x1, y1 = cur.pop(0)

    for _ in range(0, len(ranges) - 1):
        x2, y2 = cur.pop(0)

        # case 1: disjoint
        if x2 > y1 or x1 > y2:
            cur.append((x2, y2))  # add r2 back
            continue

        # case 2: r2 subset of r1
        if x2 >= x1 and y2 <= y1:
            continue

        # case 3: r1 subset of r2
        if x1 >= x2 and y1 <= y2:
            cur.append((x2, y2))  # add r2 back
            return cur

        # case 4: r2 overlap r1
        if x2 >= x1 and y2 >= y1:
            cur.append((x1, y2))
            return cur

        # case 5: r1 overlap r2
        if x1 >= x2 and y1 >= y2:
            cur.append((x2, y1))
            return cur

    # r1 was disjoint with all r2
    cur.append((x1, y1))

    return cur


cur = deepcopy(ranges)
for i in range(1000):
    cur = cycle(cur)

print(f"ans2= {sum(map(lambda r: r[1] - r[0] + 1, cur))}")

print(f"took={datetime.now() - start}")
