import random
from collections import defaultdict
from copy import deepcopy
from datetime import datetime
from pprint import pprint

from input import *  # local file, not committed


def kargers(graph):
    while len(graph) > 2:
        v1 = random.choice(list(graph.keys()))
        v2 = random.choice(graph[v1])

        new_v = f"{v1}-{v2}"

        graph[v1].extend(graph[v2])
        new_e = [n for n in graph[v1] if n not in [v1, v2]]
        if len(new_e) > 0:
            graph[new_v] = new_e

        del graph[v1]
        del graph[v2]

        for v, edges in graph.items():
            graph[v] = [e if e not in [v1, v2] else new_v for e in edges]

    return graph


graph = defaultdict(list)
for line in input.splitlines():
    if not line:
        continue

    v, conns = line.split(":")
    conns = conns.strip(" ").split(" ")

    for conn in conns:
        if conn not in graph[v]:
            graph[v].append(conn)
        if v not in graph[conn]:
            graph[conn].append(v)

attempts = 0
start = datetime.now()
while True:
    attempts += 1
    result = kargers(deepcopy(graph))
    v, e = result.popitem()
    if not len(e) == 3:
        continue

    ans = len(v.split("-")) * len(e[0].split("-"))
    print(f"attempts={attempts}, ans={ans}")
    break

print(f"took={datetime.now() - start}")
