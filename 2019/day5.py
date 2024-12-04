from copy import copy
from datetime import datetime

from inputs import input5
from intcode import run

start = datetime.now()

input = [int(i) for i in input5.split(",")]


def day5p1():
    p = copy(input)
    return run(p)


def day5p2():
    p = copy(input)
    return run(p)


if __name__ == "__main__":
    day5p1()
    day5p2()

    print(f"took={datetime.now() - start}")
