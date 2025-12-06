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

raw = open(0).read().strip().splitlines()

### PROBLEM 1 ###

data = []
for row in raw:
    parts = row.split(" ")
    keep = []
    for p in parts:
        if p != "":
            keep.append(p)
    data.append(keep)


@functools.lru_cache()
def calc(n, m, op):
    if op == "*":
        return n * m
    else:
        return n + m


ans1 = 0
for x in range(len(data[0])):
    op = data[-1][x].strip()

    num = int(data[0][x].strip())
    for y in range(1, len(data) - 1):
        num = calc(num, int(data[y][x].strip()), op)

    ans1 += num

print(f"ans1= {ans1}")


### PROBLEM 2 ###

data = []
for row in raw:
    data.append(list(row))

ops = []
for c in data[-1]:
    if c != " ":
        ops.append(c)


data.pop(-1)


empty_col = []
empty = [" " for _ in range(len(data))]
for x in range(len(data[0])):
    is_empty = True
    for y in range(len(data)):
        if data[y][x] != " ":
            is_empty = False

    if is_empty:
        empty_col.append(x)

empty_col.append(len(data[0]))

nums = []
for i, col in enumerate(empty_col):
    s = 0 if i == 0 else empty_col[i - 1] + 1

    cur = []
    for row in data:
        cur.append(row[s:col])

    nums.append(cur)


ans2 = 0
for idx, row in enumerate(nums):
    new = [[] for _ in range(len(row[0]))]
    for i in range(len(row)):
        for j in range(len(row[i])):
            new[j].append(row[i][j])

    new = list(map(lambda s: int("".join(s).strip()), new))

    op = ops[idx]

    n = new[0]

    for i in range(1, len(new)):
        n = calc(n, new[i], op)

    ans2 += n

print(f"ans2= {ans2}")

print(f"took={datetime.now() - start}")
