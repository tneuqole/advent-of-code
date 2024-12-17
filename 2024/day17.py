from collections import defaultdict
from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

program = list(map(int, data[-1].split(":")[-1].strip().split(",")))
A = int(data[0].split(":")[-1].strip())
B = int(data[1].split(":")[-1].strip())
C = int(data[2].split(":")[-1].strip())


def combo(op, A, B, C):
    if 0 <= op and op <= 3:
        return op
    elif op == 4:
        return A
    elif op == 5:
        return B
    else:
        return C


def run(A, B, C):
    i = 0
    output = []
    while i < len(program):
        ins = program[i]
        op = program[i + 1]

        if ins == 0:
            A = A // 2 ** combo(op, A, B, C)
        elif ins == 1:
            B = B ^ op
        elif ins == 2:
            B = combo(op, A, B, C) % 8
        elif ins == 3 and A != 0:
            i = op
            continue
        elif ins == 4:
            B = B ^ C
        elif ins == 5:
            output.append(combo(op, A, B, C) % 8)
        elif ins == 6:
            B = A // 2 ** combo(op, A, B, C)
        else:
            C = A // 2 ** combo(op, A, B, C)

        i += 2

    return output


print(",".join(list(map(str, run(A, B, C)))))  # p1

nums = [n for n in range(9)]
valid = defaultdict(list)
valid[-1] = [0]
for i, p in enumerate(program[::-1]):
    for a in valid[i - 1]:
        for n in nums:
            a_test = a * 8 + n

            b = a_test % 8
            b = b ^ 1
            c = a_test // 2**b
            b = b ^ c

            b = b ^ 4

            if b % 8 == p:
                valid[i].append(a_test)


a_s = []
for a in valid[15]:
    a_copy = a
    output = []
    while a > 0:
        b = a % 8
        b = b ^ 1
        c = a // 2**b
        b = b ^ c
        a = a // 8
        b = b ^ 4
        output.append(b % 8)

    if output == program:
        a_s.append(a_copy)

print(min(a_s))

print(f"took={datetime.now() - start}")
