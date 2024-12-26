from datetime import datetime

start = datetime.now()

pw = list(open(0).read().strip())

abc = "abcdefghijklmnopqrstuvwxyz"
pairs = [ch * 2 for ch in abc]
triples = [abc[i : i + 3] for i in range(0, len(abc) - 2)]


def check(pw):
    return (
        all(ch not in pw for ch in ["i", "o", "l"])
        and sum(p in pw for p in pairs) > 1
        and any(t in pw for t in triples)
    )


def inc(pw, idx):
    if idx < 0:
        return

    i = abc.index(pw[idx])
    if i == 25:
        pw[idx] = abc[0]
        inc(pw, idx - 1)
    else:
        pw[idx] = abc[i + 1]


def update(pw):
    if "i" in pw:
        i = pw.index("i")
        pw[i] = "j"
    elif "o" in pw:
        i = pw.index("o")
        pw[i] = "p"
    else:
        i = pw.index("l")
        pw[i] = "m"

    for j in range(i + 1, len(pw)):
        pw[j] = "a"


def solve(pw):
    while not check("".join(pw)):
        if any(ch in pw for ch in ["i", "o", "l"]):
            update(pw)
        else:
            inc(pw, len(pw) - 1)


solve(pw)
print("".join(pw))

inc(pw, len(pw) - 1)
solve(pw)
print("".join(pw))

print(f"took={datetime.now() - start}")
