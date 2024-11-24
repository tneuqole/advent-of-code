import functools
import itertools
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

from input import *

start = datetime.now()
rows = []
for line in input.splitlines():
    if not line:
        continue
    rows.append(line)


def calc(rows):
    sum = 0
    for y in range(len(rows)):
        weights = []
        num_rocks = 0
        for x in range(len(rows[0])):
            weight = len(rows) - x
            char = rows[x][y]
            if char == "O":
                weights.append(weight)
                num_rocks += 1
            # elif char == ".":
            #     weights.append(weight)
            elif char == "#":
                for i in range(num_rocks):
                    sum += weights[i]
                weights = []
                num_rocks = 0

        for i in range(num_rocks):
            sum += weights[i]

    return sum


def get_cols(rows):
    cols = ["" for _ in range(len(rows[0]))]
    for row in rows:
        for i, char in enumerate(row):
            cols[i] += char

    return cols


def tokenize(s):
    tokens = []
    t = ""
    for c in s:
        if c == "#":
            if t:
                tokens.append(t)
            tokens.append("#")
            t = ""
        else:
            t += c
    if t:
        tokens.append(t)

    return tokens


# left=True roll left, else roll right
def roll(rows, left):
    new = []
    for r in rows:
        parts = tokenize(r)
        new_r = ""
        for p in parts:
            if p == "#":
                new_r += "#"
                continue

            rocks = p.count("O")
            if left:
                new_r += "O" * rocks
                new_r += "." * (len(p) - rocks)
            else:
                new_r += "." * (len(p) - rocks)
                new_r += "O" * rocks

        new.append(new_r)

    return new


def cycle(rows):
    # slide north
    rows = get_cols(rows)
    rows = roll(rows, True)
    rows = get_cols(rows)

    # slide west
    rows = roll(rows, True)

    # slide south
    rows = get_cols(rows)
    rows = roll(rows, False)
    rows = get_cols(rows)

    # slide east
    rows = roll(rows, False)

    return rows


# p1
rows_copy = deepcopy(rows)

# slide north
rows_copy = get_cols(rows_copy)
rows_copy = roll(rows_copy, True)
rows_copy = get_cols(rows_copy)

print(calc(rows_copy))

# p2
seen = {tuple(rows): 0}
i = 0
cycles = 1000000000
final_cycle = 0
while i < cycles:
    rows = cycle(rows)
    i += 1

    if i == cycles:
        break

    t = tuple(rows)
    if t not in seen:
        seen[t] = i
    else:
        todo = cycles - i
        loop = i - seen[t]
        i += todo - (todo % loop)

print(calc(rows))


print(f"took={datetime.now() - start}")
