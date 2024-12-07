from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from queue import Queue

from inputs import get_program, input11
from intcode import run
from util import DIRECTIONS, replace_char, rows_to_cols

start = datetime.now()


def solve(start, panels):
    p = get_program(input11)

    painted = set()

    inp, out = Queue(), Queue()
    inp.put_nowait(start)

    x, y = 0, 0
    dir_idx = 0
    with ThreadPoolExecutor(max_workers=5) as executor:
        f = executor.submit(run, p, inp, out)

        while not f.done():
            color = out.get()
            if panels[(x, y)] is not bool(color):
                painted.add((x, y))
                panels[(x, y)] = not panels[(x, y)]

            direction = out.get()
            if direction == 1:
                # turn right
                dir_idx = dir_idx + 1 if dir_idx < 3 else 0
            else:
                # turn left
                dir_idx = dir_idx - 1 if dir_idx > 0 else 3

            x += DIRECTIONS[dir_idx][1]
            y += DIRECTIONS[dir_idx][0]

            inp.put_nowait(panels[(x, y)])

    return len(painted)


def day11p1():
    return solve(0, defaultdict(bool))


def day11p2():
    panels = defaultdict(bool)
    solve(1, panels)

    grid = ["." * 6 for _ in range(43)]
    for k, v in panels.items():
        if not v:
            continue

        replace_char(grid, k[0], k[1], "#")

    return "\n".join(rows_to_cols(grid))


if __name__ == "__main__":
    print(day11p1())
    print(day11p2())

    print(f"took={datetime.now() - start}")
