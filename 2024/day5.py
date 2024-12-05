from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open("input").read().splitlines()
rules = defaultdict(set)
for d in data:
    rules[int(d.split("|")[0])].add(int(d.split("|")[1]))

updates = open("input1").read().splitlines()


def reorder(u):
    while True:
        ordered = True
        for i in range(len(u) - 1):
            bad = rules[u[i]] & set(u[i + 1 :])
            if bad:
                ordered = False

                num = bad.pop()
                u.remove(num)
                u = u[:i] + [num] + u[i:]

                break

        if ordered:
            break

    return u[len(u) // 2]


ans1, ans2 = 0, 0
for row in updates:
    u = list(map(int, row.split(",")))
    u.reverse()

    ordered = True
    for i in range(len(u) - 1):
        if rules[u[i]] & set(u[i + 1 :]):
            ordered = False
            break

    if ordered:
        ans1 += u[len(u) // 2]
    else:
        ans2 += reorder(u)

print(ans1)
print(ans2)

print(f"took={datetime.now() - start}")
