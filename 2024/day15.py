from copy import deepcopy
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

grid = [list(r) for r in data[: data.index("")]]
moves = "".join(data[data.index("") + 1 :])

r, c = -1, -1
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "@":
            r, c = y, x


for m in moves:
    dr, dc = 0, 0
    if m == "^":
        dr = -1
    elif m == ">":
        dc = 1
    elif m == "v":
        dr = 1
    elif m == "<":
        dc = -1

    r += dr
    c += dc

    if grid[r][c] in ".@":
        continue
    elif grid[r][c] == "#":
        r -= dr
        c -= dc
        continue
    elif grid[r][c] == "O":
        nr, nc = r, c
        while True:
            nr += dr
            nc += dc
            if (
                nr < 0
                or nr >= len(grid)
                or nc < 0
                or nc >= len(grid[0])
                or grid[nr][nc] == "#"
            ):
                r -= dr
                c -= dc
                break

            if grid[nr][nc] in ".@":
                grid[nr][nc] = "O"
                grid[r][c] = "."
                break


ans1 = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "O":
            ans1 += 100 * r + c

print(ans1)


temp = [list(r) for r in data[: data.index("")]]
grid = []
for row in temp:
    newr = []
    for c in row:
        if c == "#":
            newr.extend(["#", "#"])
        elif c == ".":
            newr.extend([".", "."])
        elif c == "@":
            newr.extend(["@", "."])
        elif c == "O":
            newr.extend(["[", "]"])

    grid.append(newr)

r, c = -1, -1
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "@":
            r, c = y, x


def solve_left(grid, r, C):
    c = C.pop()
    c -= 1
    if c < 0 or grid[r][c] == "#":
        return grid

    if grid[r][c] == "]":
        grid = solve_left(grid, r, {c - 1})

    if grid[r][c] in ".@":
        grid[r][c] = "["
        grid[r][c + 1] = "]"
        grid[r][c + 2] = "."

    return grid


def solve_right(grid, r, C):
    c = C.pop()
    c += 1
    if c + 1 > len(grid[0]) or grid[r][c + 1] == "#":
        return grid

    if grid[r][c + 1] == "[":
        grid = solve_right(grid, r, {c + 1})

    if grid[r][c + 1] in ".@":
        grid[r][c + 1] = "]"
        grid[r][c] = "["
        grid[r][c - 1] = "."

    return grid


def solve_up(grid, r, C):
    r -= 1

    for c in C:
        if r < 0 or grid[r][c] == "#" or grid[r][c + 1] == "#":
            return grid

    s = False
    new_C = set()
    for c in C:
        if grid[r][c] == "[":
            new_C.add(c)
            s = True
        elif grid[r][c] == "]":
            new_C.add(c - 1)
            s = True

        if grid[r][c + 1] == "[":
            new_C.add(c + 1)
            s = True

    if s:
        grid = solve_up(grid, r, new_C)

    replace = True
    for c in C:
        if not (grid[r][c] in ".@" and grid[r][c + 1] in ".@"):
            replace = False
            break
    if replace:
        for c in C:
            grid[r][c] = "["
            grid[r][c + 1] = "]"
            grid[r + 1][c] = "."
            grid[r + 1][c + 1] = "."

    return grid


def solve_down(grid, r, C):
    r += 1

    for c in C:
        if r >= len(grid) or grid[r][c] == "#" or grid[r][c + 1] == "#":
            return grid

    s = False
    new_C = set()
    for c in C:
        if grid[r][c] == "[":
            new_C.add(c)
            s = True
        elif grid[r][c] == "]":
            new_C.add(c - 1)
            s = True

        if grid[r][c + 1] == "[":
            new_C.add(c + 1)
            s = True

    if s:
        grid = solve_down(grid, r, new_C)

    replace = True
    for c in C:
        if not (grid[r][c] in ".@" and grid[r][c + 1] in ".@"):
            replace = False
            break
    if replace:
        for c in C:
            grid[r][c] = "["
            grid[r][c + 1] = "]"
            grid[r - 1][c] = "."
            grid[r - 1][c + 1] = "."

    return grid


for m in moves:
    solvef = None
    dr, dc = 0, 0
    if m == "^":
        dr = -1
        solvef = solve_up
    elif m == ">":
        dc = 1
        solvef = solve_right
    elif m == "v":
        dr = 1
        solvef = solve_down
    else:
        dc = -1
        solvef = solve_left

    r += dr
    c += dc

    if grid[r][c] in ".@":
        continue
    elif grid[r][c] == "#":
        r -= dr
        c -= dc
        continue

    lbc = c
    if grid[r][c] == "]":
        lbc = c - 1

    ngrid = solvef(deepcopy(grid), r, {lbc})
    if ngrid == grid:
        r -= dr
        c -= dc
    else:
        grid = ngrid


ans2 = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "[":
            ans2 += 100 * r + c

print(ans2)

print(f"took={datetime.now() - start}")
