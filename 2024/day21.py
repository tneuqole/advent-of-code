import functools
import itertools
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()
codes = [code for code in data]

numpad = {
    "A": (0, 0),
    "0": (-1, 0),
    "3": (0, 1),
    "2": (-1, 1),
    "1": (-2, 1),
    "6": (0, 2),
    "5": (-1, 2),
    "4": (-2, 2),
    "9": (0, 3),
    "8": (-1, 3),
    "7": (-2, 3),
}

dirpad = {
    "A": (0, 0),
    "^": (-1, 0),
    ">": (0, -1),
    "v": (-1, -1),
    "<": (-2, -1),
}


def move(a, b, neg, pos):
    path = ""
    for _ in range(abs(a - b)):
        if a > b:
            path += neg
        else:
            path += pos

    return path


def get_moves(u, v):
    path = move(u[0], v[0], "<", ">") + move(u[1], v[1], "v", "^")
    paths = set(itertools.permutations(path))
    possible = set()
    for p in paths:
        x, y = u
        ok = True
        for m in p:
            if m == "<":
                x -= 1
            elif m == ">":
                x += 1
            elif m == "v":
                y -= 1
            elif m == "^":
                y += 1

            if (x, y) == (-2, 0):
                ok = False
                break

        if ok:
            possible.add(f"{''.join(p)}A")

    return tuple(possible)


@functools.lru_cache(maxsize=None)
def recurse(seq, u, robots, use_numpad):
    keypad = numpad if use_numpad else dirpad
    if not seq:
        return 0

    v = keypad[seq[0]]
    moves = get_moves(u, v)
    dist = -1
    if not robots:
        dist = len(min(moves, key=len))
    else:
        for m in moves:
            d = recurse(m, (0, 0), robots - 1, False)
            if dist < 0 or d < dist:
                dist = d

    return dist + recurse(seq[1:], v, robots, use_numpad)


ans1, ans2 = 0, 0
for code in codes:
    ans1 += int(code[:-1]) * recurse(code, (0, 0), 2, True)
    ans2 += int(code[:-1]) * recurse(code, (0, 0), 25, True)

print(ans1)
print(ans2)

print(f"took={datetime.now() - start}")
