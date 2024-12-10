import functools
import itertools
import re
from collections import defaultdict, deque
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

start = datetime.now()

input = open(0).read().splitlines()

grid = [list(map(int, [i for i in r])) for r in input]

# NORTH EAST SOUTH WEST
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(grid: list[list[int]], root: tuple[int], visit=True):
    E = set()
    E.add(root)

    count = 0
    q = deque()
    q.append(root)
    while len(q) > 0:
        r, c = q.popleft()
        if grid[r][c] == 9:
            count += 1
            continue

        for dr, dc in DIRS:
            rnew, cnew = r + dr, c + dc

            if (
                rnew >= 0
                and rnew < len(grid)
                and cnew >= 0
                and cnew < len(grid[0])
                and grid[rnew][cnew] == grid[r][c] + 1
            ):
                if not visit or (rnew, cnew) not in E:
                    E.add((rnew, cnew))
                    q.append((rnew, cnew))

    return count


heads = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            heads.append((r, c))

ans1, ans2 = 0, 0
for r, c in heads:
    ans1 += bfs(grid, (r, c))
    ans2 += bfs(grid, (r, c), visit=False)

print(ans1)
print(ans2)

print(f"took={datetime.now() - start}")
