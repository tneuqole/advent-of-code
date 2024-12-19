import functools
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()


@functools.lru_cache(maxsize=None)
def solve(design, towels):
    if len(design) == 0:
        return 1

    res = 0
    for t in towels:
        if design.startswith(t):
            res += solve(design[len(t) :], towels)

    return res


ans1, ans2 = 0, 0
towels = data[0].split(", ")
for design in data[2:]:
    twls = [t for t in towels if t in design]

    res = solve(design, tuple(twls))
    ans1 += int(bool(res))
    ans2 += res

print(ans1)
print(ans2)


print(f"took={datetime.now() - start}")
