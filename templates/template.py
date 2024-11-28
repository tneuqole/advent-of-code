import functools
import itertools
from collections import defaultdict, deque
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

start = datetime.now()

input = open(0).read().splitlines()
pprint(input)

print(f"took={datetime.now() - start}")
