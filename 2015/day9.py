import heapq
from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

G = defaultdict(list)
for row in data:
    a, _, b, _, dist = row.split(" ")
    G[a].append((b, int(dist)))
    G[b].append((a, int(dist)))


def dijkstra(src):
    dist = {}
    for v in G:
        dist[v] = 1e7

    dist[src] = 0

    Q = [(0, src, {src})]

    while Q:
        u_dist, u, path = heapq.heappop(Q)

        if len(path) == len(G):
            return u_dist

        for v, v_dist in G[u]:
            if v in path:
                continue

            alt = u_dist + v_dist

            if v_dist < dist[v]:
                dist[v] = alt
                heapq.heappush(Q, (alt, v, path | {v}))

    return 1e7


seen = set()


def dfs(u):
    dist = 0
    if len(seen) == len(G):
        return dist

    seen.add(u)
    for v, v_dist in G[u]:
        if v not in seen:
            dist = max(dist, dfs(v) + v_dist)

    seen.remove(u)

    return dist


shortest, longest = [], []
for v in G:
    shortest.append(dijkstra(v))
    longest.append(dfs(v))

print(min(shortest))
print(max(longest))

print(f"took={datetime.now() - start}")
