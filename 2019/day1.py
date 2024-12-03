from datetime import datetime

start = datetime.now()

input = open(0).read().splitlines()

print(sum(int(m) // 3 - 2 for m in input))

total = 0
for mass in input:
    mass = int(mass)

    f = mass // 3 - 2

    total += f
    while True:
        f = f // 3 - 2
        if f < 0:
            break
        total += f

print(total)

print(f"took={datetime.now() - start}")
