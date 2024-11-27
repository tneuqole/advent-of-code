import functools
import itertools
from copy import copy, deepcopy
from datetime import datetime
from pprint import pprint


start = datetime.now()

input = open(0).read().strip().split(",")
input = [int(i) for i in input]


def run(input: list[int]) -> int:
    i = 0
    while i < len(input):
        op = input[i]

        # add numbers from pos 1 & 2 and store result in pos 3
        if op == 1:
            pos1 = input[i + 1]
            pos2 = input[i + 2]
            pos3 = input[i + 3]

            input[pos3] = input[pos1] + input[pos2]
        # multiply numbers from pos 1 & 2 and store result in pos 3
        elif op == 2:
            pos1 = input[i + 1]
            pos2 = input[i + 2]
            pos3 = input[i + 3]

            input[pos3] = input[pos1] * input[pos2]
        elif op == 99:
            break
        else:
            # print("something went wrong")
            return 0

        i += 4

    return input[0]


# p1
p = copy(input)
p[1] = 12
p[2] = 2
print(run(p))

# p2
for i in range(100):
    for j in range(100):
        p = copy(input)
        p[1] = i
        p[2] = j
        if run(p) == 19690720:
            print(i * 100 + j)


print(f"took={datetime.now() - start}")
