from datetime import datetime
from queue import Queue

from inputs import get_program, input9
from intcode import run

start = datetime.now()


def day9p1():
    p = get_program(input9)

    inputs, outputs = Queue(), Queue()
    inputs.put_nowait(1)

    run(p, inputs, outputs)

    return outputs.get_nowait()


def day9p2():
    p = get_program(input9)

    inputs, outputs = Queue(), Queue()
    inputs.put_nowait(2)

    run(p, inputs, outputs)

    return outputs.get_nowait()


if __name__ == "__main__":
    print(day9p1())
    print(day9p2())

    print(f"took={datetime.now() - start}")
