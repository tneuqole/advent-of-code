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

graph = defaultdict(set)

for row in data:
    parts = row.split(" ")
    node = parts[0][:-1]

    for conn in parts[1:]:
        graph[node].add(conn)


ans1 = 0
q = deque()
q.append("you")

while q:
    v = q.popleft()
    if v == "out":
        ans1 += 1
        continue

    for edge in graph[v]:
        q.append(edge)

print(f"ans1= {ans1}")


@functools.cache
def search(node, has_fft, has_dac):
    if node == "out":
        return 1 if has_fft and has_dac else 0
    elif node == "fft":
        has_fft = True
    elif node == "dac":
        has_dac = True

    return sum(search(n, has_fft, has_dac) for n in graph[node])


ans2 = search("svr", False, False)

print(f"ans2= {ans2}")


print(f"took={datetime.now() - start}")
