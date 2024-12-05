from datetime import datetime

from inputs import get_program, input2
from intcode import run

start = datetime.now()


def day2p1():
    p = get_program(input2)
    p[1] = 12
    p[2] = 2
    run(p)
    return p[0]


def day2p2():
    for i in range(100):
        for j in range(100):
            p = get_program(input2)
            p[1] = i
            p[2] = j
            run(p)
            if p[0] == 19690720:
                return i * 100 + j


if __name__ == "__main__":
    print(day2p1())
    print(day2p2())

    print(f"took={datetime.now() - start}")
