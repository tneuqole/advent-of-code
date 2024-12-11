import functools
from collections import defaultdict
from datetime import datetime

start = datetime.now()

fish = list(map(int, open(0).read().strip(" ").split(",")))
counts = defaultdict(int)
for f in fish:
    counts[f] += 1


@functools.lru_cache(maxsize=None)
def calc(f: int):
    if f > 0:
        return (f - 1,)

    return (6, 8)


def solve(n, counts):
    for _ in range(n):
        new_counts = defaultdict(int)
        for f, c in counts.items():
            new = calc(f)
            for n in new:
                new_counts[n] += c

        counts = new_counts

    print(sum(counts.values()))


solve(80, counts)
solve(256, counts)

print(f"took={datetime.now() - start}")
