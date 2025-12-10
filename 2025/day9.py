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


def ints(x):
    return tuple(map(int, x.split(",")))


data = list(map(ints, open(0).read().strip().splitlines()))

ans1 = 0


def sort_points(p1, p2):
    if p1[0] < p2[0]:
        return p1, p2
    elif p1[0] > p2[0]:
        return p2, p1
    elif p1[1] < p2[1]:
        return p1, p2
    else:
        return p2, p1


areas = {}
for _ in range(len(data)):
    p1 = data.pop(0)

    for p2 in data:
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        areas[sort_points(p1, p2)] = area

areas = sorted(list(areas.items()), key=lambda item: item[1], reverse=True)

print(f"ans1= {areas[0][1]}")


print(f"took={datetime.now() - start}")
