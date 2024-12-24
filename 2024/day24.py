from datetime import datetime

start = datetime.now()

data = open(0).read().splitlines()

state = {}
idx = data.index("")
for i in range(idx):
    k, v = data[i].split(": ")
    state[k] = int(v)


def solve(state):
    Q = [data[i].split(" ") for i in range(idx + 1, len(data))]
    gates = {}
    while Q:
        in1, op, in2, _, out = Q.pop(0)

        if in1 not in state or in2 not in state:
            Q.append([in1, op, in2, "", out])
            continue

        if op == "AND":
            state[out] = int(state[in1] and state[in2])
        elif op == "OR":
            state[out] = int(state[in1] or state[in2])
        elif op == "XOR":
            state[out] = int(state[in1] != state[in2])

        gates[out] = (in1, op, in2)

    z_s = [k for k in sorted(state, reverse=True) if k.startswith("z")]

    ans = ""
    for z in z_s:
        ans += str(state[z])

    print(int(ans, 2))

    return ans, gates


actual_z, gates = solve(dict(state))

x = "".join(
    list(map(str, [state[k] for k in sorted(state, reverse=True) if k.startswith("x")]))
)
y = "".join(
    list(map(str, [state[k] for k in sorted(state, reverse=True) if k.startswith("y")]))
)

expected_z = int(x, 2) + int(y, 2)
actual_z = int(actual_z, 2)

print(bin(actual_z ^ expected_z))

print(",".join(list(sorted(["z07", "rts", "jpj", "z12", "chv", "vvw", "z26", "kgj"]))))


from graphviz import Digraph

dot = Digraph()


for k, v in state.items():
    dot.node(k, f"{k}\n{v}")

for out, g in gates.items():
    in1, op, in2 = g

    color = "black"
    if op == "AND":
        color = "red"
    elif op == "OR":
        color = "blue"
    elif op == "XOR":
        color = "green"

    dot.edge(in1, out, label=op, color=color)
    dot.edge(in2, out, label=op, color=color)

dot.render("circuit_graph", format="png", view=True)

print(f"took={datetime.now() - start}")
