import functools
import itertools
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint


start = datetime.now()

# python3 template.py < input
input = open(0).read().splitlines()
pprint(input)

print(f"took={datetime.now() - start}")
