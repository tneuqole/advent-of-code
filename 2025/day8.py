from functools import reduce
import heapq
import itertools
import math
import re
from collections import defaultdict, deque
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint
from operator import mul

start = datetime.now()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

data = list(
    map(lambda x: tuple(map(int, x.split(","))), (open(0).read().strip().splitlines()))
)


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def sort_triples(p1, p2):
    if p1[0] < p2[0]:
        return p1, p2
    elif p1[0] > p2[0]:
        return p2, p1
    elif p1[1] < p2[1]:
        return p1, p2
    elif p1[1] > p2[1]:
        return p2, p1
    elif p1[2] < p2[2]:
        return p1, p2
    else:
        return p2, p1


pairs = {}
for _ in range(len(data)):
    p1 = data.pop(0)

    for p2 in data:
        pairs[sort_triples(p1, p2)] = dist(p1, p2)

    data.append(p1)


all_pairs = sorted(list(pairs.items()), key=lambda item: item[1])

shortest = list(
    map(
        lambda x: list(x[0]),
        all_pairs[:1000],
    )
)

for _ in range(1000):
    box1 = shortest.pop(0)

    keep = []
    for box2 in shortest:
        conn = False
        for p in box2:
            if p in box1:
                conn = True
                break
        if conn:
            box1.extend(box2)
        else:
            keep.append(box2)

    keep.append(box1)
    shortest = keep


ans1 = reduce(mul, (sorted(list(map(len, map(set, shortest))), reverse=True)[:3]))

print(f"ans1= {ans1}")


path = set()
cur = all_pairs[0]
for i in range(len(all_pairs)):
    cur = all_pairs[i]
    path.add(cur[0][0])
    path.add(cur[0][1])

    if len(path) == len(data):
        break

ans2 = cur[0][0][0] * cur[0][1][0]

print(f"ans2= {ans2}")

print(f"took={datetime.now() - start}")
