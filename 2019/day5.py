from collections import deque
from datetime import datetime

from inputs import get_program, input5
from intcode import run

start = datetime.now()


def day5p1():
    p = get_program(input5)
    return run(p, inputs=deque([1]))


def day5p2():
    p = get_program(input5)
    return run(p, inputs=deque([5]))


if __name__ == "__main__":
    day5p1()
    day5p2()

    print(f"took={datetime.now() - start}")
