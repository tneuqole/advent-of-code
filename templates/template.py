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

data = open(0).read().splitlines()
pprint(data)

print(f"took={datetime.now() - start}")
