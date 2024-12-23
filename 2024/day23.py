import functools
from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

computers = defaultdict(set)
for row in data:
    c1, c2 = row.split("-")
    computers[c1].add(c2)
    computers[c2].add(c1)


triples = set()
for c1, conns1 in computers.items():
    for c2, conns2 in computers.items():
        if c1 == c2:
            continue

        if c1 not in conns2 and c2 not in conns1:
            continue

        for c3 in conns1 & conns2:
            triples.add(tuple(sorted([c1, c2, c3])))


print(len([c for c in triples if c[0][0] == "t" or c[1][0] == "t" or c[2][0] == "t"]))


@functools.cache
def solve(c1, conns):
    conns = set(conns)
    if c1 in conns:
        return conns

    conns.add(c1)
    result = set(conns)
    for c2 in computers[c1]:
        if conns - computers[c2]:
            continue

        n_conns = solve(c2, tuple(conns))
        if len(n_conns) > len(result):
            result = n_conns

    return result


longest = []
for c in computers:
    conns = solve(c, ())
    if len(conns) > len(longest):
        longest = conns

print(",".join(sorted(longest)))


print(f"took={datetime.now() - start}")
