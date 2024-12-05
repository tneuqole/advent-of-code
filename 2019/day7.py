import itertools
from collections import deque
from copy import copy
from datetime import datetime

from inputs import get_program, input7
from intcode import run

start = datetime.now()


test1 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
test2 = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"


def day7p1():
    p = get_program(input7)
    ans = 0
    for seq in itertools.permutations("01234"):
        a = run(copy(p), inputs=deque([int(seq[0]), 0]))[0]
        b = run(copy(p), inputs=deque([int(seq[1]), a]))[0]
        c = run(copy(p), inputs=deque([int(seq[2]), b]))[0]
        d = run(copy(p), inputs=deque([int(seq[3]), c]))[0]
        e = run(copy(p), inputs=deque([int(seq[4]), d]))[0]

        if e > ans:
            ans = e

    return ans


def day7p2():
    pass


if __name__ == "__main__":
    print(day7p1())
    day7p2()

    print(f"took={datetime.now() - start}")
