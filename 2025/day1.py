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

data = open(0).read().splitlines()

dial = 50
CLICKS = 100

ans1 = 0
ans2 = 0
for move in data:
    clicks = int(move[1:])
    dir = -1 if move[0] == "L" else 1
    for i in range(0, clicks):
        dial += dir
        if dial == 0:
            ans2 += 1
        elif dial == 100:
            dial = 0
            ans2 += 1
        elif dial == -1:
            dial = 99

    if dial == 0:
        ans1 += 1

print(f"p1= {ans1}")
print(f"p2= {ans2}")

print(f"took={datetime.now() - start}")
