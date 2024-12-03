from datetime import datetime

start = datetime.now()

input = open(0).read().splitlines()

s_x, s_y = -1, -1
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == "S":
            s_x = x
            s_y = y

coords = [[s_x, s_y]]
x, y = s_x + 1, s_y
dir = "R"  # right, left, up, down
while not (x == s_x and y == s_y):
    coords.append([x, y])
    c = input[y][x]

    if c == "|":
        if dir == "D":
            y += 1
        else:
            y -= 1
    elif c == "-":
        if dir == "R":
            x += 1
        else:
            x -= 1
    elif c == "7":
        if dir == "R":
            y += 1
            dir = "D"
        else:
            x -= 1
            dir = "L"
    elif c == "J":
        if dir == "D":
            x -= 1
            dir = "L"
        else:
            y -= 1
            dir = "U"
    elif c == "F":
        if dir == "U":
            x += 1
            dir = "R"
        else:
            y += 1
            dir = "D"
    elif c == "L":
        if dir == "D":
            x += 1
            dir = "R"
        else:
            y -= 1
            dir = "U"

print(len(coords) / 2)

# shoelace formula
area = 0
for i in range(len(coords) - 1):
    area += (coords[i][0] * coords[i + 1][1]) - (coords[i + 1][0] * coords[i][1])

area += (coords[-1][0] * coords[0][1]) - (coords[-1][1] * coords[0][0])
area = abs(int(area / 2))

# pick's theorem
print(area + 1 - (len(coords) / 2))

print(f"took={datetime.now() - start}")
