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

ans1 = 0
ans2 = 0
for row in data:
    b = list(row)

    # find first max
    l, l_idx = -1, 0
    for i in range(0, len(b)):
        cur = int(b[i])
        if cur > l:
            l = cur
            l_idx = i

    # find second max
    r = -1
    if l_idx < len(b) - 1:
        for i in range(l_idx + 1, len(b)):
            cur = int(b[i])
            if cur > r:
                r = cur
        ans1 += int(f"{l}{r}")
    else:
        for i in range(l_idx - 1, -1, -1):
            cur = int(b[i])
            if cur > r:
                r = cur
        ans1 += int(f"{r}{l}")

    to_remove = len(b) - 12
    for _ in range(to_remove):
        lowest = 10
        idx = -1
        for i in range(1, len(b)):
            cur = int(b[i])
            if cur > int(b[i - 1]):
                idx = i - 1
                break
            if cur <= lowest:
                lowest = cur
                idx = i

        b = b[0:idx] + b[idx + 1 : len(b)]

    ans2 += int("".join(b))


print(f"ans1= {ans1}")
print(f"ans2= {ans2}")
print(f"took={datetime.now() - start}")
