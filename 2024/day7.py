import itertools
from datetime import datetime

start = datetime.now()


data = [
    (int(r.split(":")[0]), list(map(int, r.split(":")[1].strip().split(" "))))
    for r in open(0).read().splitlines()
]  # lol


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def combine(x, y):
    return int(f"{x}{y}")


def solve(funcs):
    ans = 0
    for k, v in data:
        combos = list(itertools.product(funcs, repeat=len(v) - 1))
        for ops in combos:
            res = v[0]
            for i in range(1, len(v)):
                res = ops[i - 1](res, v[i])

            if res == k:
                ans += res
                break

    print(ans)


solve([add, mul])
solve([add, mul, combine])

print(f"took={datetime.now() - start}")
