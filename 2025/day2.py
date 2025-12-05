import functools
import heapq
import itertools
import math
import re
from collections import defaultdict, deque
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

start = datetime.now()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

data = open(0).read().strip().split(",")


def test(x, y, i, regex, nums):
    match = re.match(regex, str(i))

    if not match:
        return

    num = int(match[0])

    if x <= num and num <= y:
        nums.add(int(num))


nums1 = set()
nums2 = set()
for interval in data:
    x, y = map(int, interval.split("-"))

    for i in range(x, y + 1):
        test(x, y, i, r"(\d+)\1", nums1)
        test(x, y, i, r"(\d+)\1+", nums2)
        test(x, y, i, r"(\d+?)\1+", nums2)

print(f"ans1= {sum(nums1)}")
# print(nums2)
print(f"ans2= {sum(nums2)}")

print(f"took={datetime.now() - start}")
