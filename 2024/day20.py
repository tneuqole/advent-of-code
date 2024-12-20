import heapq
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def manhattan(u, v):
    return abs(u[1] - v[1]) + abs(u[0] - v[0])


def get_neighbors(grid, u, offset):
    n = set()
    for r in range(u[0] - offset, u[0] + offset + 1):
        for c in range(u[1] - offset, u[1] + offset + 1):
            if (
                r >= 0
                and r < len(grid)
                and c >= 0
                and c < len(grid[0])
                and grid[r][c] != "#"
                and u != (r, c)
                and manhattan(u, (r, c)) <= offset
            ):
                n.add((r, c))

    return n


def dijkstra(grid, src, dest):
    dist, prev = {}, {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            dist[(r, c)] = 1e7

    dist[src] = 0

    Q = [(0, src)]

    while Q:
        u_dist, u = heapq.heappop(Q)

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

            v = (r, c)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (alt, v))

    return 0, []


grid = [[""] * len(data[0]) for _ in range(len(data))]
sr, sc, er, ec = -1, -1, -1, -1
for r in range(len(data)):
    for c in range(len(data[0])):
        grid[r][c] = data[r][c]

        if grid[r][c] == "S":
            sr, sc = r, c

        if grid[r][c] == "E":
            er, ec = r, c


dist, prev = dijkstra(grid, (sr, sc), (er, ec))

path = {}
u = (er, ec)
while u:
    path[u] = dist - len(path)
    u = prev.get(u)


ans1, ans2 = 0, 0
T = 100
for u, u_dist in path.items():
    n = get_neighbors(grid, u, 2)
    for v in n:
        v_dist = path[v]

        if abs(u_dist - v_dist) - manhattan(u, v) >= T:
            ans1 += 1

    n = get_neighbors(grid, u, 20)
    for v in n:
        v_dist = path[v]

        if abs(u_dist - v_dist) - manhattan(u, v) >= T:
            ans2 += 1

print(ans1 // 2)
print(ans2 // 2)


print(f"took={datetime.now() - start}")
