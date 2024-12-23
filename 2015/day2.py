from datetime import datetime

start = datetime.now()


data = open(0).read().splitlines()

ans1, ans2 = 0, 0

for row in data:
    l, w, h = map(int, row.split("x"))
    ans1 += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, l * h, w * h)
    ans2 += min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h) + l * w * h

print(ans1)
print(ans2)

print(f"took={datetime.now() - start}")
