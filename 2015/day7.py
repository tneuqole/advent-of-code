from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

state = {"1": 1}
gates = []

for row in data:
    row.replace(" -> ", " ")
    parts = row.split(" ")
    if len(parts) == 3:
        try:
            state[parts[2]] = int(parts[0])
        except ValueError:
            gates.append(parts)
    else:
        gates.append(parts)


def solve(state, gates):
    while gates:
        gate = gates.pop(0)

        if len(gate) == 3:
            a, _, b = gate
            if a in state:
                state[b] = state[a]
            else:
                gates.append(gate)
        elif len(gate) == 4:
            assert gate[0] == "NOT"
            _, a, _, b = gate
            if a in state:
                state[b] = ~state[a]
            else:
                gates.append(gate)
        elif len(gate) == 5:
            a, op, b, _, c = gate
            if a in state and op == "RSHIFT":
                state[c] = state[a] >> int(b)
            elif a in state and op == "LSHIFT":
                state[c] = state[a] << int(b)
            elif a in state and b in state:
                if op == "AND":
                    state[c] = state[a] & state[b]
                elif op == "OR":
                    state[c] = state[a] | state[b]
            else:
                gates.append(gate)

    return state["a"]


a = solve(dict(state), list(gates))
print(a)

state["b"] = a
print(solve(state, gates))


print(f"took={datetime.now() - start}")
