from copy import copy
from datetime import datetime

start = datetime.now()

input = open(0).read().splitlines()


def check(nums):
    if not (nums[0] < nums[1]):
        nums.reverse()

    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if not (1 <= diff and diff <= 3):
            return 0

    return 1


ans1, ans2 = 0, 0
for line in input:
    nums = [int(n) for n in line.split(" ")]

    ans1 += check(nums)

    for i in range(len(nums)):
        n = copy(nums)
        n.pop(i)
        if check(n) == 1:
            ans2 += 1
            break

print(ans1)
print(ans2)

print(f"took={datetime.now() - start}")
