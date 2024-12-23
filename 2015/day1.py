from datetime import datetime

start = datetime.now()

data = open(0).read()

print(data.count("(") - data.count(")"))

for i in [idx + 1 for idx, ch in enumerate(data) if ch == ")"]:
    if data[:i].count("(") - data[:i].count(")") == -1:
        print(i)
        break

print(f"took={datetime.now() - start}")
