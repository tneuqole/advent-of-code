import itertools
from datetime import datetime

start = datetime.now()


def check(num, p2=False):
    if len(set(num)) == len(num):
        return 0

    for i in range(len(num) - 1):
        if int(num[i + 1]) - int(num[i]) < 0:
            return 0

    if p2:
        return 1 if 2 in [len(list(g)) for _, g in itertools.groupby(num)] else 0

    return 1


print(sum(check(str(i)) for i in range(240298, 784956 + 1)))
print(sum(check(str(i), p2=True) for i in range(240298, 784956 + 1)))

print(f"took={datetime.now() - start}")
