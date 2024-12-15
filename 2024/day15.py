from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

grid = [list(r) for r in data[: data.index("")]]
moves = "".join(data[data.index("") + 1 :])


def find_robot(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return r, c


def gps(grid, ch):
    ans = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ch:
                ans += 100 * r + c

    return ans


def move_left(grid, r, C):
    c = C.pop()
    c -= 1
    if c < 0 or grid[r][c] == "#":
        return

    if grid[r][c] == "]":
        move_left(grid, r, {c - 1})

    if grid[r][c] in ".@":
        grid[r][c] = "["
        grid[r][c + 1] = "]"
        grid[r][c + 2] = "."


def move_right(grid, r, C):
    c = C.pop()
    c += 1
    if c + 1 > len(grid[0]) or grid[r][c + 1] == "#":
        return

    if grid[r][c + 1] == "[":
        move_right(grid, r, {c + 1})

    if grid[r][c + 1] in ".@":
        grid[r][c + 1] = "]"
        grid[r][c] = "["
        grid[r][c - 1] = "."


def move_up(grid, r, C):
    r -= 1

    for c in C:
        if r < 0 or grid[r][c] == "#" or grid[r][c + 1] == "#":
            return

    recurse = False
    new_C = set()
    for c in C:
        if grid[r][c] == "[":
            new_C.add(c)
            recurse = True
        elif grid[r][c] == "]":
            new_C.add(c - 1)
            recurse = True

        if grid[r][c + 1] == "[":
            new_C.add(c + 1)
            recurse = True

    if recurse:
        move_up(grid, r, new_C)

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


def move_down(grid, r, C):
    r += 1

    for c in C:
        if r >= len(grid) or grid[r][c] == "#" or grid[r][c + 1] == "#":
            return

    recurse = False
    new_C = set()
    for c in C:
        if grid[r][c] == "[":
            new_C.add(c)
            recurse = True
        elif grid[r][c] == "]":
            new_C.add(c - 1)
            recurse = True

        if grid[r][c + 1] == "[":
            new_C.add(c + 1)
            recurse = True

    if recurse:
        move_down(grid, r, new_C)

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


DIRS = {
    "^": (-1, 0, move_up),
    ">": (0, 1, move_right),
    "v": (1, 0, move_down),
    "<": (0, -1, move_left),
}

r, c = find_robot(grid)
for m in moves:
    dr, dc, _ = DIRS[m]

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


print(gps(grid, "O"))


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

r, c = find_robot(grid)
for m in moves:
    dr, dc, move_func = DIRS[m]

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
        lbc -= 1

    hash = str(grid)
    move_func(grid, r, {lbc})
    if str(grid) == hash:
        r -= dr
        c -= dc


print(gps(grid, "["))

print(f"took={datetime.now() - start}")
