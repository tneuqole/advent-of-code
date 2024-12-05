from datetime import datetime
from queue import Queue

from inputs import get_program, input5
from intcode import run

start = datetime.now()


def day5p1():
    p = get_program(input5)

    inputs, outputs = Queue(), Queue()
    inputs.put_nowait(1)
    run(p, inputs, outputs)

    return list(outputs.queue)


def day5p2():
    p = get_program(input5)

    inputs, outputs = Queue(), Queue()
    inputs.put_nowait(5)
    run(p, inputs, outputs)

    return outputs.get_nowait()


if __name__ == "__main__":
    print(day5p1())
    print(day5p2())

    print(f"took={datetime.now() - start}")
