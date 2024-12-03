from collections import defaultdict
from copy import copy
from datetime import datetime

from input import *

start = datetime.now()
mirrors = []
mirror = []
for line in input.splitlines():
    if not line:
        if mirror:
            mirrors.append(mirror)
        mirror = []
        continue

    mirror.append(line)

mirrors.append(mirror)


h_lines = defaultdict(int)
v_lines = defaultdict(int)


def calc1(mirror, factor, h, idx):
    for i in range(len(mirror) - 1):
        if not mirror[i] == mirror[i + 1]:
            continue

        is_mirror = True
        l = i - 1
        r = i + 2

        while l >= 0 and r < len(mirror):
            if not mirror[l] == mirror[r]:
                is_mirror = False
                break

            l -= 1
            r += 1

        if is_mirror:
            if h:
                h_lines[idx] = i + 1
            else:
                v_lines[idx] = i + 1

            return (i + 1) * factor

    return 0


def calc2(mirror, factor, h, idx):
    for i in range(len(mirror) - 1):
        if not mirror[i] == mirror[i + 1]:
            continue

        is_mirror = True
        l = i - 1
        r = i + 2

        while l >= 0 and r < len(mirror):
            if not mirror[l] == mirror[r]:
                is_mirror = False
                break

            l -= 1
            r += 1

        if is_mirror:
            if h and i + 1 == h_lines[idx]:
                is_mirror = False
            elif not h and i + 1 == v_lines[idx]:
                is_mirror = False
            else:
                return (i + 1) * factor
    return 0


# p1
sum = 0
for idx, m in enumerate(mirrors):
    sum += calc1(m, 100, True, idx)

    cols = ["" for _ in range(len(m[0]))]
    for row in m:
        for i, char in enumerate(row):
            cols[i] += char

    sum += calc1(cols, 1, False, idx)

print(sum)
print(f"took={datetime.now() - start}")


# p2
start = datetime.now()
sum = 0
for idx, m in enumerate(mirrors):
    found = False
    for x in range(len(m)):
        for y in range(len(m[0])):
            m_copy = copy(m)
            if m[x][y] == "#":
                new = list(m_copy[x])
                new[y] = "."
                m_copy[x] = "".join(new)
            else:
                new = list(m_copy[x])
                new[y] = "#"
                m_copy[x] = "".join(new)

            val = calc2(m_copy, 100, True, idx)
            if val > 0:
                found = True
                sum += val
                break

            cols = ["" for _ in range(len(m_copy[0]))]
            for row in m_copy:
                for i, char in enumerate(row):
                    cols[i] += char

            val = calc2(cols, 1, False, idx)
            if val > 0:
                found = True
                sum += val
                break

        if found:
            break

    assert found

print(sum)
print(f"took={datetime.now() - start}")
