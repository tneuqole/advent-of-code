import sys
from collections import defaultdict
from datetime import datetime

sys.setrecursionlimit(2000)

start = datetime.now()

DIRS = {
    ".": [(-1, 0), (0, 1), (1, 0), (0, -1)],
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
}


grid = [[col for col in row] for row in open(0).read().splitlines()]
src = (0, 1)
dest = (len(grid) - 1, len(grid[0]) - 2)

J = []
seen = set()


def dfs1(root, dest):
    if root == dest:
        return 0

    max_len = 0
    r, c = root
    seen.add(root)
    count = 0
    for dr, dc in DIRS[grid[r][c]]:
        rnew, cnew = r + dr, c + dc
        if (
            rnew >= 0
            and rnew < len(grid)
            and cnew >= 0
            and cnew < len(grid[0])
            and grid[rnew][cnew] != "#"
            and (rnew, cnew) not in seen
        ):
            count += 1
            max_len = max(max_len, dfs1((rnew, cnew), dest) + 1)
    seen.remove(root)

    if count > 1 and root not in J:
        J.append(root)

    return max_len


print(dfs1(src, dest))  # p1


edges = defaultdict(set)
edge_lens = {}


def bfs(root):
    Q = [(root[0], root[1], [root])]

    while Q:
        r, c, path = Q.pop(0)

        if (r, c) in J and (r, c) != root:
            edges[path[0]].add((r, c))
            edge_lens[(path[0], (r, c))] = len(path) - 1
            continue

        count = 0
        for dr, dc in DIRS["."]:
            rnew, cnew = r + dr, c + dc
            if (
                rnew >= 0
                and rnew < len(grid)
                and cnew >= 0
                and cnew < len(grid[0])
                and grid[rnew][cnew] != "#"
                and (rnew, cnew) not in path
            ):
                count += 1
                Q.append((rnew, cnew, path + [(rnew, cnew)]))


for j in J:
    bfs(j)


seen = set()


def dfs2(src):
    if src == J[-1]:
        return 0

    max_len = -1
    seen.add(src)
    for e in edges[src]:
        if e in seen:
            continue
        max_len = max(max_len, dfs2(e) + edge_lens[(src, e)])
    seen.remove(src)

    return max_len


J.reverse()
print(dfs2(J[0]) + dfs1(src, J[0]) + dfs1(J[-1], dest))  # p2


print(f"took={datetime.now() - start}")
