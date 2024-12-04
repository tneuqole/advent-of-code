# interpret parameter as position (index in memory)
POSITION_MODE = "0"

# interpret parameter as value
IMMEDIATE_MODE = "1"


def run(program: list[int]) -> int:
    i = 0
    while i < len(program):
        ins = str(program[i])
        ins = "0" * (5 - len(ins)) + ins

        op = int(ins[3:])
        modes = ins[:3]

        # addition: program[p3] = p1 + p2
        if op == 1:
            p1 = program[i + 1]
            p2 = program[i + 2]
            pos = program[i + 3]

            x = program[p1] if modes[2] == POSITION_MODE else p1
            y = program[p2] if modes[1] == POSITION_MODE else p2

            program[pos] = x + y

            i += 4
        # multiplication: program[p3] = p1 * p2
        elif op == 2:
            p1 = program[i + 1]
            p2 = program[i + 2]
            pos = program[i + 3]

            x = program[p1] if modes[2] == POSITION_MODE else p1
            y = program[p2] if modes[1] == POSITION_MODE else p2

            program[pos] = x * y

            i += 4
        # stdin: program[p1] = input()
        elif op == 3:
            pos = program[i + 1]
            program[pos] = int(input("> "))

            i += 2
        # stdout: print(program[p1])
        elif op == 4:
            pos = program[i + 1]
            print(program[pos])

            i += 2
        # jump if truthy: i = p2 if p1
        elif op == 5:
            p1 = program[i + 1]
            p2 = program[i + 2]

            x = program[p1] if modes[2] == POSITION_MODE else p1
            jump_to = program[p2] if modes[1] == POSITION_MODE else p2

            if x > 0:
                i = jump_to
            else:
                i += 3
        # jump if falsely: i = p2 if not p1
        elif op == 6:
            p1 = program[i + 1]
            p2 = program[i + 2]

            x = program[p1] if modes[2] == POSITION_MODE else p1
            jump_to = program[p2] if modes[1] == POSITION_MODE else p2

            if x == 0:
                i = jump_to
            else:
                i += 3
        # less than: program[p3] = 1 if p1 < p2 else 0
        elif op == 7:
            p1 = program[i + 1]
            p2 = program[i + 2]
            pos = program[i + 3]

            x = program[p1] if modes[2] == POSITION_MODE else p1
            y = program[p2] if modes[1] == POSITION_MODE else p2

            program[pos] = 1 if x < y else 0

            i += 4
        # equals: program[p3] = 1 if p1 == p2 else 0
        elif op == 8:
            p1 = program[i + 1]
            p2 = program[i + 2]
            pos = program[i + 3]

            x = program[p1] if modes[2] == POSITION_MODE else p1
            y = program[p2] if modes[1] == POSITION_MODE else p2

            program[pos] = 1 if x == y else 0

            i += 4
        elif op == 99:
            break
        else:
            print(f"something went wrong, ins={ins}")
            return 0

    return program[0]
