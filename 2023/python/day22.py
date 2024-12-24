from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

cubes = []
for row in data:
    xyz = row.split("~")
    cubes.append(
        (
            tuple(map(int, xyz[0].split(","))),
            tuple(map(int, xyz[1].split(","))),
        )
    )

cubes = sorted(cubes, key=lambda x: x[0][2])


def orientation(a, b, c):
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if val > 0:
        return 1  # clockwise
    elif val < 0:
        return 2  # counterclockwise
    else:
        return 0  # collinear


def collinear_intersect(a, b, c):
    if (
        (b[0] <= max(a[0], c[0]))
        and (b[0] >= min(a[0], c[0]))
        and (b[1] <= max(a[1], c[1]))
        and (b[1] >= min(a[1], c[1]))
    ):
        return True
    return False


def intersect(a, b, c, d):
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if (o1 != o2) and (o3 != o4):
        return True

    if (o1 == 0) and collinear_intersect(a, c, b):
        return True

    if (o2 == 0) and collinear_intersect(a, d, b):
        return True

    if (o3 == 0) and collinear_intersect(c, a, d):
        return True

    if (o4 == 0) and collinear_intersect(c, b, d):
        return True

    return False


def overlap(c1, cubes):
    for c2 in cubes:
        if intersect(c1[0], c1[1], c2[0], c2[1]):
            return True

    return False


def simulate(cubes):
    simulated = defaultdict(set)
    for c1 in cubes:
        inserted = False
        for z in sorted(simulated, reverse=True):
            if overlap(c1, simulated[z]):
                simulated[z + 1].add(c1)
                simulated[z + 1 + c1[1][2] - c1[0][2]].add(c1)
                inserted = True
                break

        if not inserted:
            simulated[1].add(c1)
            simulated[1 + c1[1][2] - c1[0][2]].add(c1)

    return simulated


sim1 = simulate(cubes)
supports, supported_by = defaultdict(set), defaultdict(set)
for i in range(1, len(sim1)):
    for c1 in sim1[i]:
        for c2 in sim1[i + 1]:
            if c1 == c2:
                continue

            if overlap(c1, [c2]):
                supports[c1].add(c2)
                supported_by[c2].add(c1)

ans1 = len([c for c in cubes if c not in supports])
fall = []
for c1 in supports:
    if all(len(supported_by[c2]) > 1 for c2 in supports[c1]):
        ans1 += 1
    else:
        fall.append(c1)

print(ans1)

ans2 = 0
fall.sort(key=lambda x: x[0][2])
for cube in fall:
    c_copy = list(cubes)
    c_copy.remove(cube)

    sim2 = simulate(c_copy)

    diff = set()
    for k, v in sim1.items():
        diff.update(sim2[k] - v)

    ans2 += len(diff)

print(ans2)

print(f"took={datetime.now() - start}")
