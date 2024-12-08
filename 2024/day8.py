import itertools
from collections import defaultdict
from datetime import datetime

start = datetime.now()

grid = [r for r in open(0).read().splitlines()]

antennas = defaultdict(list)
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == ".":
            continue
        antennas[ch].append((r, c))


def solve(p2=False):
    max_r, max_c = len(grid), len(grid[0])
    antinodes = set()
    for _, v in antennas.items():
        for c1, c2 in list(itertools.combinations(v, 2)):
            r_dist, c_dist = abs(c1[0] - c2[0]), abs(c1[1] - c2[1])

            c1_mods, c2_mods = [], []
            if c1[0] > c2[0]:
                c1_mods.append(1)
                c2_mods.append(-1)
            else:
                c1_mods.append(-1)
                c2_mods.append(1)

            if c1[1] > c2[1]:
                c1_mods.append(1)
                c2_mods.append(-1)
            else:
                c1_mods.append(-1)
                c2_mods.append(1)

            if p2:
                antinodes.add(c1)
                antinodes.add(c2)

            while True:
                c1 = (c1[0] + (r_dist) * c1_mods[0]), c1[1] + (c_dist * c1_mods[1])

                if 0 <= c1[0] and c1[0] < max_r and 0 <= c1[1] and c1[1] < max_c:
                    antinodes.add(c1)
                else:
                    break

                if not p2:
                    break

            while True:
                c2 = (c2[0] + (r_dist) * c2_mods[0]), c2[1] + (c_dist * c2_mods[1])
                if 0 <= c2[0] and c2[0] < max_r and 0 <= c2[1] and c2[1] < max_c:
                    antinodes.add(c2)
                else:
                    break

                if not p2:
                    break

    print(len(antinodes))


solve()
solve(p2=True)

print(f"took={datetime.now() - start}")
