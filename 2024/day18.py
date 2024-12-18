import heapq
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

M = 70
B = 1024


def dijkstra(grid, src, dest):
    dist, prev = {}, {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                continue
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

    return 0, None


grid = [["." for _ in range(M + 1)] for _ in range(M + 1)]
for i in range(B):
    c, r = map(int, data[i].split(","))
    grid[r][c] = "#"


ans, _ = dijkstra(grid, (0, 0), (M, M))
print(ans)

i = B
while True:
    c, r = map(int, data[i].split(","))
    grid[r][c] = "#"

    ans, _ = dijkstra(grid, (0, 0), (M, M))
    if ans == 0:
        print(data[i])
        break

    i += 1


print(f"took={datetime.now() - start}")
