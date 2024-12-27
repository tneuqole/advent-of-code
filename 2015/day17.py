import itertools
from datetime import datetime

start = datetime.now()

nums = list(map(int, open(0).read().splitlines()))

ans1 = 0
min_c = 1e7
for i in range(1, len(nums) + 1):
    for c in itertools.combinations(nums, i):
        if sum(c) == 150:
            min_c = min(min_c, i)
            ans1 += 1

ans2 = 0
for c in itertools.combinations(nums, min_c):
    if sum(c) == 150:
        ans2 += 1

print(ans2)

print(f"took={datetime.now() - start}")
