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

data = open(0).read().strip().splitlines()
pprint(data)

ans1, ans2 = 0, 0

print(f"ans1= {ans1}")
print(f"ans2= {ans2}")

print(f"took={datetime.now() - start}")
