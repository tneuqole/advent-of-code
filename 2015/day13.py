from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

E = defaultdict(int)
G = defaultdict(set)

for row in data:
    parts = row.strip(".").split(" ")
    a, b, w = parts[0], parts[-1], int(parts[3])
    if parts[2] == "lose":
        w *= -1
    E[tuple(sorted([a, b]))] += w
    G[a].add(b)
    G[b].add(a)


seen = []


def dfs(u):
    dist = 0

    seen.append(u)
    for v in G[u]:
        if v not in seen:
            dist = max(dist, dfs(v) + E[tuple(sorted([u, v]))])
        elif len(seen) == len(G) and seen[0] == v:
            dist += E[tuple(sorted([u, v]))]

    seen.remove(u)

    return dist


print(dfs(list(G.keys())[0]))

for k in dict(G):
    G[k].add("myself")
    G["myself"].add(k)
    E[tuple(sorted([k, "myself"]))] = 0

print(dfs(list(G.keys())[0]))

print(f"took={datetime.now() - start}")
