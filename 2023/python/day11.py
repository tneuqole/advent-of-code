from itertools import combinations

from input import *

data = []
column_idx = set()
factor = 1000000
blank_rows = []
for line in input.splitlines():
    if not line:
        continue

    # expand rows with no galaxies
    if "#" not in line:
        blank_rows.append(len(data))

    data.append(line)

    # keep track of which columns have a galaxy
    [column_idx.add(i) for i, c in enumerate(line) if c == "#"]


blank_cols = [i for i in range(len(data[0])) if i not in column_idx]

# get coords of all galaxies
coords = []
for y in range(len(data)):
    x_s = [i for i, c in enumerate(data[y]) if c == "#"]
    coords.extend([(x, y) for x in x_s])

# for each pair, calulate distance based on coords
# d = abs(x1 - x2 + y1 - y2)
sum = 0
for c1, c2 in list(combinations(coords, 2)):
    sum += abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

    x_max = max(c1[0], c2[0])
    x_min = min(c1[0], c2[0])
    for i in blank_cols:
        if x_min < i and i < x_max:
            sum += max(1, factor - 1)

    y_max = max(c1[1], c2[1])
    y_min = min(c1[1], c2[1])
    for i in blank_rows:
        if y_min < i and i < y_max:
            sum += max(1, factor - 1)

print(sum)
