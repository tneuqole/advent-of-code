from copy import copy
from datetime import datetime

from inputs import input2
from intcode import run

start = datetime.now()

input = [int(i) for i in input2.split(",")]


def day2p1():
    p = copy(input)
    p[1] = 12
    p[2] = 2
    return run(p)


def day2p2():
    for i in range(100):
        for j in range(100):
            p = copy(input)
            p[1] = i
            p[2] = j
            if run(p) == 19690720:
                return i * 100 + j


if __name__ == "__main__":
    print(day2p1())
    print(day2p2())

    print(f"took={datetime.now() - start}")
