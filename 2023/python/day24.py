import itertools
from datetime import datetime

start = datetime.now()

stones = [
    list(map(int, row.replace(" @", ",").split(", ")))
    for row in open(0).read().splitlines()
]

MIN = 200000000000000
MAX = 400000000000000


ans1 = 0
for s1, s2 in itertools.combinations(stones, 2):
    px1, py1, _, vx1, vy1, _ = s1
    px2, py2, _, vx2, vy2, _ = s2
    try:
        a = (py1 * vx2 - py2 * vx2 - px1 * vy2 + px2 * vy2) / (vx1 * vy2 - vy1 * vx2)
        b = (vx1 * a + px1 - px2) / vx2
    except ZeroDivisionError:
        continue

    x = a * vx1 + px1
    y = b * vy2 + py2
    if MIN <= x <= MAX and MIN <= y <= MAX and a > 0 and b > 0:
        ans1 += 1


print(ans1)  # p1

# ty :D https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kxqjg33/
s0, s1, s2 = stones[0:3]

p1 = [s1[i] - s0[i] for i in range(3)]
v1 = [s1[i] - s0[i] for i in range(3, 6)]
p2 = [s2[i] - s0[i] for i in range(3)]
v2 = [s2[i] - s0[i] for i in range(3, 6)]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]


t1 = -(dot(cross(p1, p2), v2)) / dot(cross(v1, p2), v2)
t2 = -(dot(cross(p1, p2), v1)) / dot(cross(p1, v2), v1)

c1 = [s1[i] + t1 * s1[i + 3] for i in range(3)]
c2 = [s2[i] + t2 * s2[i + 3] for i in range(3)]

v = [(c2[i] - c1[i]) / (t2 - t1) for i in range(3)]
p = [c1[i] - t1 * v[i] for i in range(3)]

print(int(sum(p)))  # p2

print(f"took={datetime.now() - start}")
