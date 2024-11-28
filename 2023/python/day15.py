import functools
import itertools
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint

start = datetime.now()

input = open(0).read().splitlines()


def calc_hash(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256

    return val


print(sum(calc_hash(s) for s in input[0].split(",")))

# each box will have a list of {op: fl}
boxes = [[] for i in range(256)]
for ins in input[0].split(","):
    if "=" in ins:
        op, fl = ins.split("=")
        box_num = calc_hash(op)

        replaced = False
        for i, entry in enumerate(boxes[box_num]):
            if op in entry:
                boxes[box_num][i] = {op: fl}
                replaced = True
                break
        if not replaced:
            boxes[box_num].append({op: fl})

    else:
        op = ins[:-1]
        box_num = calc_hash(op)
        for i, entry in enumerate(boxes[box_num]):
            if op in entry:
                boxes[box_num].remove(entry)
                break

ans = 0
for i, box in enumerate(boxes):
    for j, entry in enumerate(box):
        ans += (i + 1) * (j + 1) * int(list(entry.values())[0])

print(ans)
print(f"took={datetime.now() - start}")
