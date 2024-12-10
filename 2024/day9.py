from datetime import datetime

start = datetime.now()

data = open(0).read().strip()


disk = []
i, id = 0, 0
while i < len(data) - 1:
    disk.extend([str(id) for _ in range(int(data[i]))])
    disk.extend("." * int(data[i + 1]))
    i += 2
    id += 1

disk.extend([str(id) for _ in range(int(data[i]))])


s, e = 0, len(disk) - 1
while s < e:
    while disk[s] != ".":
        s += 1

    while disk[e] == ".":
        e -= 1

    if s > e:
        break

    disk[s] = disk[e]
    disk[e] = "."


print(sum(i * int(id) for i, id in enumerate(disk) if id != "."))


disk, files, free_space = [], [], []
is_file = True
for d in list(map(int, [n for n in data])):
    if is_file:
        files.append((len(disk), d))
        disk.extend([len(files) - 1] * d)
    else:
        free_space.append((len(disk), d))
        disk.extend([-1] * d)

    is_file = not is_file


for file in files[::-1]:
    for i, free in enumerate(free_space):
        if free[1] < file[1]:
            continue

        file_idx = file[0]
        free_idx = free[0]

        if file_idx < free_idx:
            break

        for _ in range(file[1]):
            disk[free_idx] = disk[file_idx]
            disk[file_idx] = -1
            file_idx += 1
            free_idx += 1

        free_space[i] = (free[0] + file[1], free[1] - file[1])
        break


print(sum(i * d for i, d in enumerate(disk) if d > 0))

print(f"took={datetime.now() - start}")
