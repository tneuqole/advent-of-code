from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

locks = []
keys = []


def parse_key(key):
    k = [-1 for _ in range(5)]
    for r, row in enumerate(key[1:]):
        for c, ch in enumerate(row):
            if ch == "#" and k[c] == -1:
                k[c] = 5 - r

    keys.append(k)


def parse_lock(lock):
    l = [-1 for _ in range(5)]
    for r, row in enumerate(lock[1:]):
        for c, ch in enumerate(row):
            if ch == "." and l[c] == -1:
                l[c] = r
    locks.append(l)


i = 0
while i < len(data):
    obj = data[i : i + 7]
    if obj[0] == ".....":
        parse_key(obj)
    else:
        parse_lock(obj)

    i += 8

count = 0
for key in keys:
    for lock in locks:
        if all(key[i] + lock[i] <= 5 for i in range(5)):
            count += 1

print(count)

print(f"took={datetime.now() - start}")
