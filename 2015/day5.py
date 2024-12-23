import itertools
from datetime import datetime

start = datetime.now()


data = open(0).read().splitlines()


good = [c * 2 for c in "abcdefghijklmnopqrstuvwxyz"]
bad = ["ab", "cd", "pq", "xy"]


def check(s, lst):
    for x in lst:
        if x in s:
            return True
    return False


nice = 0
for s in data:
    if check(s, bad):
        continue
    if not check(s, good):
        continue

    if s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") < 3:
        continue

    nice += 1

print(nice)

pairs = set(
    "".join(s)
    for s in list(
        itertools.combinations_with_replacement("abcdefghijklmnopqrstuvwxyz", 2)
    )
    + list(
        itertools.combinations_with_replacement("abcdefghijklmnopqrstuvwxyz"[::-1], 2)
    )
)

triples = set()
for s in [c * 3 for c in "abcdefghijklmnopqrstuvwxyz"]:
    for ch in "abcdefghijklmnopqrstuvwxyz":
        triples.add(f"{s[0]}{ch}{s[2]}")


def check_pairs(s):
    for p in pairs:
        if s.count(p) > 1:
            return True

    return False


nice = 0
for s in data:
    if not check(s, triples):
        continue

    if not check_pairs(s):
        continue

    nice += 1

print(nice)

print(f"took={datetime.now() - start}")
