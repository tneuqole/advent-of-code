import queue


def parse_param(mode: str, param: int, program: list[int], relative_base: int) -> int:
    # position mode
    if mode == "0":
        extend_memory(program, param)
        return program[param]
    # immediate mode
    elif mode == "1":
        return param
    # relative mode
    elif mode == "2":
        pos = param + relative_base
        extend_memory(program, pos)
        return program[pos]
    else:
        print(f"parse_mode: something went wrong, mode={mode}")
        exit()


def get_pos(mode: str, param: int, relative_base: int) -> int:
    if mode == "0":
        return param
    elif mode == "2":
        return param + relative_base
    else:
        print(f"get_pos: something went wrong, mode={mode}")
        exit()


def extend_memory(program: list[int], pos: int):
    if pos < len(program):
        return

    program.extend([0 for _ in range(pos - len(program) + 1)])


def run(program: list[int], inputs: queue.Queue, outputs: queue.Queue):
    i, relative_base = 0, 0
    while i < len(program):
        ins = str(program[i])
        ins = "0" * (5 - len(ins)) + ins

        op = int(ins[3:])
        modes = ins[:3]

        # addition: program[p3] = p1 + p2
        if op == 1:
            p1 = program[i + 1]
            p2 = program[i + 2]
            p3 = program[i + 3]

            x = parse_param(modes[2], p1, program, relative_base)
            y = parse_param(modes[1], p2, program, relative_base)
            pos = get_pos(modes[0], p3, relative_base)
            extend_memory(program, pos)

            program[pos] = x + y

            i += 4
        # multiplication: program[p3] = p1 * p2
        elif op == 2:
            p1 = program[i + 1]
            p2 = program[i + 2]
            p3 = program[i + 3]

            x = parse_param(modes[2], p1, program, relative_base)
            y = parse_param(modes[1], p2, program, relative_base)
            pos = get_pos(modes[0], p3, relative_base)
            extend_memory(program, pos)

            program[pos] = x * y

            i += 4
        # stdin: program[p1] = input()
        elif op == 3:
            p1 = program[i + 1]

            pos = get_pos(modes[2], p1, relative_base)
            extend_memory(program, pos)

            program[pos] = inputs.get()

            i += 2
        # stdout: print(program[p1])
        elif op == 4:
            p1 = program[i + 1]

            x = parse_param(modes[2], p1, program, relative_base)

            outputs.put_nowait(x)

            i += 2
        # jump if truthy: i = p2 if p1
        elif op == 5:
            p1 = program[i + 1]
            p2 = program[i + 2]

            x = parse_param(modes[2], p1, program, relative_base)
            jump_to = parse_param(modes[1], p2, program, relative_base)

            if x > 0:
                i = jump_to
            else:
                i += 3
        # jump if falsely: i = p2 if not p1
        elif op == 6:
            p1 = program[i + 1]
            p2 = program[i + 2]

            x = parse_param(modes[2], p1, program, relative_base)
            jump_to = parse_param(modes[1], p2, program, relative_base)

            if x == 0:
                i = jump_to
            else:
                i += 3
        # less than: program[p3] = 1 if p1 < p2 else 0
        elif op == 7:
            p1 = program[i + 1]
            p2 = program[i + 2]
            p3 = program[i + 3]

            x = parse_param(modes[2], p1, program, relative_base)
            y = parse_param(modes[1], p2, program, relative_base)
            pos = get_pos(modes[0], p3, relative_base)
            extend_memory(program, pos)

            program[pos] = 1 if x < y else 0

            i += 4
        # equals: program[p3] = 1 if p1 == p2 else 0
        elif op == 8:
            p1 = program[i + 1]
            p2 = program[i + 2]
            p3 = program[i + 3]

            x = parse_param(modes[2], p1, program, relative_base)
            y = parse_param(modes[1], p2, program, relative_base)
            pos = get_pos(modes[0], p3, relative_base)
            extend_memory(program, pos)

            program[pos] = 1 if x == y else 0

            i += 4
        # adjust relative base
        elif op == 9:
            p1 = program[i + 1]

            relative_base += parse_param(modes[2], p1, program, relative_base)

            i += 2
        # halt
        elif op == 99:
            break
        else:
            print(f"run: something went wrong, ins={ins}")
            exit()
