from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()


class Reindeer:
    def __init__(self, id, v, t, w):
        self.id = id
        self.v = v
        self.t = t
        self.w = w
        self.state = True
        self.t_left = t
        self.points = 0
        self.dist = 0


R = list(
    Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[13]))
    for row in data
    for parts in [row.split(" ")]
)

for _ in range(2503):
    for r in R:
        if r.state:
            r.dist += r.v

        r.t_left -= 1
        if r.t_left == 0:
            r.state = not r.state
            r.t_left = r.t if r.state else r.w

    d = max(R, key=lambda r: r.dist).dist
    for r in R:
        if r.dist == d:
            r.points += 1

print(max(R, key=lambda r: r.dist).dist)
print(max(R, key=lambda r: r.points).points)

print(f"took={datetime.now() - start}")
