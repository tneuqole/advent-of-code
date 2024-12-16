import heapq
from copy import deepcopy
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

grid = [[c for c in row] for row in data]

sr, sc, er, ec = -1, -1, -1, -1
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            sr, sc = r, c

        if grid[r][c] == "E":
            er, ec = r, c


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dijkstra(grid, src, dest):
    dist, prev = {}, {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                continue
            dist[(r, c)] = 1e7

    dist[src] = 0

    Q = [(0, src, DIRS[2])]

    while Q:
        u_dist, u, dr = heapq.heappop(Q)

        if u_dist > dist[u]:
            continue

        if u == dest:
            return u_dist, prev

        for d in DIRS:
            r, c = u[0] + d[0], u[1] + d[1]
            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or grid[r][c] == "#"
            ):
                continue

            alt = dist[u] + 1
            if d != dr:
                alt += 1000

            v = (r, c)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (alt, v, d))

    return 0, None


dist, prev = dijkstra(grid, (sr, sc), (er, ec))
print(dist)  # p1

u = (er, ec)
s = set()
while u is not None:
    s.add(u)
    u = prev.get(u)

s2 = deepcopy(s)
for r, c in s:
    if grid[r][c] not in "SE":
        grid[r][c] = "#"
        n_dist, prev = dijkstra(grid, (sr, sc), (er, ec))
        if n_dist == dist:
            u = (er, ec)
            while u is not None:
                s2.add(u)
                u = prev.get(u)

        grid[r][c] = "."

print(len(s2))  # p2


print(f"took={datetime.now() - start}")
