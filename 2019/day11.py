from datetime import datetime
from queue import Queue

from inputs import get_program, input11
from intcode import run

start = datetime.now()


def day2p1():
    p = get_program(input11)
    run(p, Queue(), Queue())


def day2p2():
    pass


if __name__ == "__main__":
    print(day2p1())
    print(day2p2())

    print(f"took={datetime.now() - start}")
