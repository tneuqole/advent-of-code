import itertools
from concurrent.futures import ThreadPoolExecutor
from copy import copy
from datetime import datetime
from queue import Queue

from inputs import get_program, input7
from intcode import run

start = datetime.now()


def day7p1():
    p = get_program(input7)
    ans = 0
    for seq in itertools.permutations("01234"):
        a_inputs, a_outputs = Queue(), Queue()
        a_inputs.put_nowait(int(seq[0]))
        a_inputs.put_nowait(0)

        run(copy(p), a_inputs, a_outputs)

        b_inputs, b_outputs = Queue(), Queue()
        b_inputs.put_nowait(int(seq[1]))
        b_inputs.put_nowait(a_outputs.get_nowait())

        run(copy(p), b_inputs, b_outputs)

        c_inputs, c_outputs = Queue(), Queue()
        c_inputs.put_nowait(int(seq[2]))
        c_inputs.put_nowait(b_outputs.get_nowait())

        run(copy(p), c_inputs, c_outputs)

        d_inputs, d_outputs = Queue(), Queue()
        d_inputs.put_nowait(int(seq[3]))
        d_inputs.put_nowait(c_outputs.get_nowait())

        run(copy(p), d_inputs, d_outputs)

        e_inputs, e_outputs = Queue(), Queue()
        e_inputs.put_nowait(int(seq[4]))
        e_inputs.put_nowait(d_outputs.get_nowait())

        run(copy(p), e_inputs, e_outputs)

        res = e_outputs.get_nowait()
        if res > ans:
            ans = res

    return ans


def day7p2():
    ans = 0
    for seq in itertools.permutations("56789"):
        p_a = get_program(input7)
        p_b = copy(p_a)
        p_c = copy(p_a)
        p_d = copy(p_a)
        p_e = copy(p_a)

        q_a = Queue()
        q_a.put_nowait(int(seq[0]))
        q_a.put_nowait(0)

        q_b = Queue()
        q_b.put_nowait(int(seq[1]))

        q_c = Queue()
        q_c.put_nowait(int(seq[2]))

        q_d = Queue()
        q_d.put_nowait(int(seq[3]))

        q_e = Queue()
        q_e.put_nowait(int(seq[4]))

        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.submit(run, p_a, q_a, q_b)
            executor.submit(run, p_b, q_b, q_c)
            executor.submit(run, p_c, q_c, q_d)
            executor.submit(run, p_d, q_d, q_e)
            executor.submit(run, p_e, q_e, q_a)

        res = q_a.get_nowait()
        if res > ans:
            ans = res

    return ans


if __name__ == "__main__":
    print(day7p1())
    print(day7p2())

    print(f"took={datetime.now() - start}")
