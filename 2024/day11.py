import functools
from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read()

stones = list(map(int, data.strip().split(" ")))


@functools.lru_cache(maxsize=None)
def calc(s: int):
    if s == 0:
        return (1,)

    st = str(s)
    l = len(st)
    if l % 2 == 0:
        return (int(st[: l // 2]), int(st[l // 2 :]))

    return (s * 2024,)


def solve(n, counts):
    for _ in range(n):
        new_counts = defaultdict(int)
        for stone, count in counts.items():
            res = calc(stone)
            for s in res:
                new_counts[s] += count

        counts = new_counts

    print(sum(counts.values()))


counts = defaultdict(int)
for stone in stones:
    counts[stone] += 1

solve(25, counts)
solve(75, counts)

print(f"took={datetime.now() - start}")
