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


def ints(x):
    return list(map(int, x[1:-1].split(",")))


data = []
for row in raw:
    parts = row.split(" ")

    lights = parts[0][1:-1]
    buttons = list(map(ints, parts[1:-1]))
    joltage_req = ints(parts[-1])

    data.append([lights, buttons, joltage_req])

ans1 = 0
for lights, buttons, _ in data:
    state = list("." * len(lights))

    q = deque()
    for i in range(len(buttons)):
        q.append((copy(state), buttons[i], 0))

    while q:
        cur, btn, count = q.popleft()

        # print(cur, btn, count)

        for i in btn:
            if cur[i] == "#":
                cur[i] = "."
            else:
                cur[i] = "#"

        count += 1

        if "".join(cur) == lights:
            ans1 += count
            break

        for i in range(len(buttons)):
            q.append((copy(cur), buttons[i], count))

print(f"ans1= {ans1}")

print(f"took={datetime.now() - start}")
