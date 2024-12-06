from copy import copy
from datetime import datetime

start = datetime.now()

grid = open(0).read().splitlines()


# NORTH EAST SOUTH WEST
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


x, y = -1, -1
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "^":
            x, y = r, c


def p1(r, c):
    d = DIRS[0]
    seen = set([(r, c)])
    while True:
        r += d[0]
        c += d[1]
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            break

        if grid[r][c] != "#":
            seen.add((r, c))
            continue

        r -= d[0]
        c -= d[1]
        d = DIRS[DIRS.index(d) + 1] if DIRS.index(d) != 3 else DIRS[0]

    return seen


def p2(r_start, c_start, coords):
    ans = 0
    for i, j in coords:
        g = copy(grid)
        d = DIRS[0]
        r, c = r_start, c_start
        seen = set([r, c])

        row = list(g[i])
        row[j] = "#"
        g[i] = "".join(row)

        blockers = {DIRS[0]: set(), DIRS[1]: set(), DIRS[2]: set(), DIRS[3]: set()}
        loop = False
        while not loop:
            r += d[0]
            c += d[1]
            if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]):
                break

            if g[r][c] != "#":
                seen.add((r, c))
                continue

            if (r, c) in blockers[d]:
                loop = True

            blockers[d].add((r, c))

            r -= d[0]
            c -= d[1]
            d = DIRS[DIRS.index(d) + 1] if DIRS.index(d) != 3 else DIRS[0]

        ans += int(loop)

    print(ans)


seen = p1(x, y)
print(len(seen))

p2(x, y, seen)

print(f"took={datetime.now() - start}")
