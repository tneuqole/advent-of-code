from copy import deepcopy
from datetime import datetime

start = datetime.now()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

grid = [[col for col in row] for row in open(0).read().splitlines()]

H = len(grid)
W = len(grid[0])

corners = [(0, 0), (0, W - 1), (H - 1, 0), (H - 1, W - 1)]


def solve(grid, p2=False):
    for _ in range(100):
        new_g = [["." for _ in range(W)] for _ in range(H)]
        if p2:
            for r, c in corners:
                new_g[r][c] = "#"

        for r in range(H):
            for c in range(W):
                if p2:
                    if (r, c) in corners:
                        continue

                n = 0
                for dr, dc in DIRS:
                    newr, newc = r + dr, c + dc
                    if newr < 0 or newr >= H or newc < 0 or newc >= W:
                        continue

                    n += 1 if grid[newr][newc] == "#" else 0

                if grid[r][c] == "#":
                    if 2 <= n <= 3:
                        new_g[r][c] = "#"
                    else:
                        new_g[r][c] = "."
                elif n == 3:
                    new_g[r][c] = "#"
                else:
                    new_g[r][c] = "."

        grid = new_g

    print(sum(["".join(row).count("#") for row in grid]))


solve(deepcopy(grid))

for r, c in corners:
    grid[r][c] = "#"

solve(grid, p2=True)

print(f"took={datetime.now() - start}")
