import heapq
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()
grid = [[int(c) for c in r] for r in data]

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
OPP = {(-1, 0): (1, 0), (0, 1): (0, -1), (1, 0): (-1, 0), (0, -1): (0, 1)}

H = len(grid) - 1
W = len(grid[0]) - 1


def dijkstra1(grid, src, dest):
    Q = [(0, src, (0, 0), 0)]

    seen = set()
    while Q:
        u_dist, u, cur_d, steps = heapq.heappop(Q)

        if u == dest:
            return u_dist

        if (u, cur_d, steps) in seen:
            continue

        seen.add((u, cur_d, steps))

        for new_d in DIRS:
            if new_d == OPP.get(cur_d):
                continue

            r, c = u[0] + new_d[0], u[1] + new_d[1]
            v = (r, c)
            new_steps = steps + 1 if cur_d == new_d else 1
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or new_steps > 3:
                continue

            v_dist = u_dist + grid[r][c]

            heapq.heappush(
                Q,
                (v_dist, v, new_d, new_steps),
            )

    return -1, []


def colinear(a, b, c, d, e):
    return a[0] == b[0] == c[0] == d[0] == e[0] or a[1] == b[1] == c[1] == d[1] == e[1]


def dijkstra2(grid, src, dest):
    Q = [(0, src, (1, 0), 0, [src]), (0, src, (0, 1), 0, [src])]

    seen = set()
    while Q:
        u_dist, u, cur_d, steps, path = heapq.heappop(Q)

        if u == dest:
            if colinear(*path[-5:]):
                return u_dist

        if (u, cur_d, steps) in seen:
            continue

        seen.add((u, cur_d, steps))

        if steps < 4:
            r, c = u[0] + cur_d[0], u[1] + cur_d[1]
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue
            heapq.heappush(
                Q,
                (u_dist + grid[r][c], (r, c), cur_d, steps + 1, path + [(r, c)]),
            )
            continue

        for new_d in DIRS:
            if new_d == OPP.get(cur_d):
                continue

            r, c = u[0] + new_d[0], u[1] + new_d[1]
            v = (r, c)
            new_steps = steps + 1 if cur_d == new_d else 1
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or new_steps > 10:
                continue

            v_dist = u_dist + grid[r][c]

            heapq.heappush(
                Q,
                (v_dist, v, new_d, new_steps, path + [v]),
            )

    return -1


print(dijkstra1(grid, (0, 0), (H, W)))
print(dijkstra2(grid, (0, 0), (H, W)))


print(f"took={datetime.now() - start}")
