import functools
import itertools
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

from input import *

start = datetime.now()
for line in test_input.splitlines():
    if not line:
        continue

print(f"took={datetime.now() - start}")
