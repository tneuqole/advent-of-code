from datetime import datetime

start = datetime.now()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid = [[col for col in row] for row in open(0).read().splitlines()]
root = next(
    (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "S"
)

STEPS = 26501365
SIZE = len(grid)


def bfs(grid, root, limit):
    E = {root}
    Q = [(root[0], root[1], 0)]

    valid = set()
    while Q:
        r, c, depth = Q.pop(0)
        if depth % 2 == limit % 2:
            valid.add((r, c))

        if depth == limit:
            continue

        for dr, dc in DIRS:
            rnew, cnew = r + dr, c + dc
            if grid[rnew % SIZE][cnew % SIZE] in ".S" and (rnew, cnew) not in E:
                E.add((rnew, cnew))
                Q.append((rnew, cnew, depth + 1))

    return len(valid)


print(bfs(grid, root, 64))

vals = []
n = SIZE // 2
for i in range(3):
    vals.append(bfs(grid, root, n + SIZE * i))

c = vals[0]
a = (vals[2] - 2 * vals[1] + c) // 2
b = vals[1] - a - c

x = (STEPS - n) // SIZE
print(a * x**2 + b * x + c)

print(f"took={datetime.now() - start}")
