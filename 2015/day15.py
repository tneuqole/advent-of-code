import functools
import operator
import re
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

ing = []
for row in data:
    ing.append(list(map(int, re.findall(r"-?\d+", row))))

ans1, ans2 = 0, 0
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            for l in range(1, 100):
                if i + j + k + l != 100:
                    continue

                vals = [
                    ing[0][idx] * i
                    + ing[1][idx] * j
                    + ing[2][idx] * k
                    + ing[3][idx] * l
                    for idx in range(4)
                ]

                if any(v <= 0 for v in vals):
                    continue

                res = functools.reduce(operator.mul, vals)
                ans1 = max(ans1, res)

                cals = ing[0][4] * i + ing[1][4] * j + ing[2][4] * k + ing[3][4] * l
                if cals == 500:
                    ans2 = max(ans2, res)

print(ans1)
print(ans2)

print(f"took={datetime.now() - start}")
