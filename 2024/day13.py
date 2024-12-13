from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()


def solve(f):
    i, ans = 0, 0
    while i < len(data):
        ax = int(data[i].split(" ")[2][2:-1])
        ay = int(data[i].split(" ")[3][2:])
        bx = int(data[i + 1].split(" ")[2][2:-1])
        by = int(data[i + 1].split(" ")[3][2:])
        px = int(data[i + 2].split(" ")[1][2:-1]) + f
        py = int(data[i + 2].split(" ")[2][2:]) + f

        # axA + bxB = px, ayA + byB = py

        # multiply eq1 * ay, eq2 * ax
        # ayaxA + aybxB = aypx, axayA + axbyB = axpy

        # subtract eq2 - eq1
        # axayA + axbyB - ayaxA - aybxB = axpy - aypx

        # B = (axpy - aypx) / (axby - aybx)

        B = (ax * py - ay * px) // (ax * by - ay * bx)
        A = (px - B * bx) // ax

        if A * ax + B * bx == px and A * ay + B * by == py:
            ans += A * 3 + B * 1

        i += 4

    print(ans)


solve(0)
solve(10000000000000)

print(f"took={datetime.now() - start}")
