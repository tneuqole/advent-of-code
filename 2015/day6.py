from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

lights = defaultdict(bool)
brightness = defaultdict(int)
for row in data:
    parts = row.split(" ")

    if parts[1] in ["on", "off"]:
        state = True if parts[1] == "on" else False
        inc = 1 if parts[1] == "on" else -1
        x1, y1 = map(int, parts[2].split(","))
        x2, y2 = map(int, parts[-1].split(","))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = state
                brightness[(x, y)] = max(brightness[(x, y)] + inc, 0)
    else:
        x1, y1 = map(int, parts[1].split(","))
        x2, y2 = map(int, parts[-1].split(","))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = not lights[(x, y)]
                brightness[(x, y)] += 2


print(list(lights.values()).count(True))
print(sum(brightness.values()))

print(f"took={datetime.now() - start}")
