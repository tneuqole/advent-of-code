from collections import defaultdict
from copy import deepcopy
from datetime import datetime

start = datetime.now()

data = open(0).read().strip().split("\n")
idx = data.index("")

rules = defaultdict(list)
for i in range(idx):
    id, r = data[i].split("{")
    r = r[:-1].split(",")
    rules[id] = r


def gt(a, b):
    return a > b


def lt(a, b):
    return a < b


def recurse(x, m, a, s, id):
    nums = {"x": x, "m": m, "a": a, "s": s}
    funcs = {"<": lt, ">": gt}
    for r in rules[id]:
        if "<" in r or ">" in r:
            idx = r.index(":")
            if funcs[r[1]](nums[r[0]], int(r[2:idx])):
                res = r[idx + 1 :]
                if res == "A":
                    return 1
                elif res == "R":
                    return 0
                else:
                    return recurse(x, m, a, s, res)
        elif r == "A":
            return 1
        elif r == "R":
            return 0
        else:
            return recurse(x, m, a, s, r)


ans1 = 0
for i in range(idx + 1, len(data)):
    nums = data[i].split(",")

    x = int(nums[0][3:])
    m = int(nums[1][2:])
    a = int(nums[2][2:])
    s = int(nums[3][2:-1])

    if recurse(x, m, a, s, "in"):
        ans1 += x + m + a + s

print(ans1)


class Node:
    def __init__(self, cond):
        self.cond = cond
        self.children = []

    def add(self, node):
        self.children.append(node)


def build_tree(rls):
    r = rls[0]
    if "<" in r or ">" in r:
        parts = r.split(":")
        n = Node(parts[0])
        if parts[1] == "A":
            n.add(Node(True))
        elif parts[1] == "R":
            n.add(Node(False))
        else:
            n.add(build_tree(rules[parts[1]]))

        n.add(build_tree(rls[1:]))

        return n

    if r == "A":
        return Node(True)
    elif r == "R":
        return Node(False)
    else:
        return build_tree(rules[r])


def traverse(root, bounds, idx):
    if type(root.cond) is bool:
        if not root.cond:
            bounds[idx] = None
        return

    num = root.cond[0]
    op = root.cond[1]
    val = int(root.cond[2:])

    cur = bounds[idx][num][op]
    n_idx = len(bounds)
    bounds.append(deepcopy(bounds[idx]))
    if op == ">":
        new = max(val, cur)
        bounds[idx][num][op] = new
        bounds[n_idx][num]["<"] = new + 1
    elif op == "<":
        new = min(val, cur)
        bounds[idx][num][op] = new
        bounds[n_idx][num][">"] = new - 1

    traverse(root.children[0], bounds, idx)
    traverse(root.children[1], bounds, n_idx)


bounds = [
    {
        "x": {">": 0, "<": 4001},
        "m": {">": 0, "<": 4001},
        "a": {">": 0, "<": 4001},
        "s": {">": 0, "<": 4001},
    }
]

root = build_tree(rules["in"])
traverse(root, bounds, 0)

ans2 = 0
for b in bounds:
    if not b:
        continue
    ans2 += (
        (b["x"]["<"] - 1 - (b["x"][">"] + 1) + 1)
        * (b["m"]["<"] - 1 - (b["m"][">"] + 1) + 1)
        * (b["a"]["<"] - 1 - (b["a"][">"] + 1) + 1)
        * (b["s"]["<"] - 1 - (b["s"][">"] + 1) + 1)
    )

print(ans2)

print(f"took={datetime.now() - start}")
