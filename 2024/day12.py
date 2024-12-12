from collections import defaultdict, deque
from datetime import datetime

start = datetime.now()

grid = open(0).read().splitlines()

coords = defaultdict(list)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(grid: list[str], root: tuple[int, int]):
    E = set()
    E.add(root)

    q = deque()
    q.append(root)
    while len(q) > 0:
        r, c = q.popleft()

        for dr, dc in DIRS:
            rnew, cnew = r + dr, c + dc

            if (
                rnew >= 0
                and rnew < len(grid)
                and cnew >= 0
                and cnew < len(grid[0])
                and grid[rnew][cnew] == grid[r][c]
            ):
                if (rnew, cnew) not in E:
                    E.add((rnew, cnew))
                    q.append((rnew, cnew))

    return E


plants = []
seen = set()
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if (r, c) in seen:
            continue
        visited = bfs(grid, (r, c))
        seen.update(visited)
        plants.append((grid[r][c], visited))


ans1, ans2 = 0, 0
for a, cs in plants:
    p = []
    pc = []
    sides = 0
    for r, c in cs:
        p.extend(
            [
                (r - 1, c),
                (r, c + 1),
                (r + 1, c),
                (r, c - 1),
            ],
        )

        # find number of corners, inner and outer
        # outer
        # TL
        if (r - 1, c) not in cs and (r, c - 1) not in cs:
            sides += 1

        # TR
        if (r - 1, c) not in cs and (r, c + 1) not in cs:
            sides += 1

        # BL
        if (r + 1, c) not in cs and (r, c - 1) not in cs:
            sides += 1

        # BR
        if (r + 1, c) not in cs and (r, c + 1) not in cs:
            sides += 1

        # inside
        # TL
        if (r - 1, c) in cs and (r, c - 1) in cs and (r - 1, c - 1) not in cs:
            sides += 1

        # TR
        if (r - 1, c) in cs and (r, c + 1) in cs and (r - 1, c + 1) not in cs:
            sides += 1

        # BL
        if (r + 1, c) in cs and (r, c - 1) in cs and (r + 1, c - 1) not in cs:
            sides += 1

        # BR
        if (r + 1, c) in cs and (r, c + 1) in cs and (r + 1, c + 1) not in cs:
            sides += 1

    ans1 += len([c for c in p if c not in cs]) * len(cs)
    ans2 += sides * len(cs)

print(ans1)
print(ans2)
print(f"took={datetime.now() - start}")
