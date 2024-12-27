from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

want = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

aunts = defaultdict(dict)
for row in data:
    parts = row.replace(",", ":").split(": ")

    id = parts[0].strip().split(" ")[1]
    for i in range(1, len(parts), 2):
        aunts[id][parts[i].strip()] = int(parts[i + 1].strip())

for aunt, vals in aunts.items():
    ok1, ok2 = True, True
    for k, v in vals.items():
        if want[k] != v:
            ok1 = False

        if k == "cats" and want[k] >= v:
            ok2 = False
        elif k == "trees" and want[k] >= v:
            ok2 = False
        elif k == "pomeranians" and want[k] <= v:
            ok2 = False
        elif k == "goldfish" and want[k] <= v:
            ok2 = False

        if k not in ["cats", "trees", "pomeranians", "goldfish"] and want[k] != v:
            ok2 = False

    if ok1:
        print(aunt)
    if ok2:
        print(aunt)

print(f"took={datetime.now() - start}")
