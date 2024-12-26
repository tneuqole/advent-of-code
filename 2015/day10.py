from datetime import datetime

start = datetime.now()

data = open(0).read().strip()


def separate(s):
    parts = []
    p = s[0]
    i = 1
    while i < len(s):
        if s[i] != p[0]:
            parts.append(p)
            p = s[i]
        else:
            p += s[i]

        i += 1

    parts.append(p)

    return parts


def solve(i, s):
    for _ in range(i):
        parts = separate(s)
        new = ""
        for p in parts:
            new += f"{p.count(p[0])}{p[0]}"

        s = new

    return s


s = solve(40, data)
print(len(s))
print(len(solve(10, s)))

print(f"took={datetime.now() - start}")
