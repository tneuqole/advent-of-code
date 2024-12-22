import math
from copy import deepcopy
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

ff, conj, brdcst = {}, {}, []
for row in data:
    idx = row.index("->")
    name = row[:idx].strip()
    dest = [x.strip() for x in row[idx + 2 :].strip().split(",")]

    if name == "broadcaster":
        brdcst = dest
        continue

    if name[0] == "%":
        ff[name[1:]] = [False, dest]
    else:
        conj[name[1:]] = [{}, dest]

for m, state in ff.items():
    for dest in state[1]:
        if dest in conj:
            conj[dest][0][m] = False

for m, state in conj.items():
    for dest in state[1]:
        if dest in conj:
            conj[dest][0][m] = False


def solve(brdcst, ff, conj, p2=False):
    rx_src = set(
        [m for m in conj if "cs" in conj[m][1]] + [m for m in ff if "cs" in ff[m][1]]
    )
    cycles = []

    high, low, count = 0, 0, 0
    while count < 1000 or p2:
        low += 1
        count += 1
        Q = [("brdcst", False, m) for m in brdcst]
        while Q:
            src, pulse, dest = Q.pop(0)
            if pulse:
                high += 1
            else:
                low += 1

            if dest == "rx":
                continue

            if dest in ff:
                if pulse:
                    continue

                m = ff[dest]
                m[0] = not m[0]
                for d in m[1]:
                    Q.append((dest, m[0], d))

                ff[dest] = m
            else:
                m = conj[dest]
                m[0][src] = pulse

                emit = False if False not in m[0].values() else True
                for d in m[1]:
                    Q.append((dest, emit, d))

                conj[dest] = m

                if dest in rx_src and emit:
                    cycles.append(count)
                    rx_src.remove(dest)

        if not rx_src:
            print(math.lcm(*cycles))
            return

    print(high * low * 1000**2)


solve(brdcst, deepcopy(ff), deepcopy(conj))
solve(brdcst, deepcopy(ff), deepcopy(conj), p2=True)


print(f"took={datetime.now() - start}")
