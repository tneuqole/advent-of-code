from datetime import datetime

start = datetime.now()

input = open(0).read().splitlines()


ans1 = 0
max_r = len(input)
max_c = len(input[0])
for r in range(max_r):
    for c in range(max_c):
        if input[r][c] != "X":
            continue

        # E
        if c + 3 < max_c and (
            input[r][c] + input[r][c + 1] + input[r][c + 2] + input[r][c + 3] == "XMAS"
        ):
            ans1 += 1

        # W
        if c - 3 >= 0 and (
            input[r][c] + input[r][c - 1] + input[r][c - 2] + input[r][c - 3] == "XMAS"
        ):
            ans1 += 1

        # N
        if r - 3 >= 0 and (
            input[r][c] + input[r - 1][c] + input[r - 2][c] + input[r - 3][c] == "XMAS"
        ):
            ans1 += 1
        # S
        if r + 3 < max_r and (
            input[r][c] + input[r + 1][c] + input[r + 2][c] + input[r + 3][c] == "XMAS"
        ):
            ans1 += 1

        # NE
        if (
            r - 3 >= 0
            and c + 3 < max_c
            and (
                input[r][c]
                + input[r - 1][c + 1]
                + input[r - 2][c + 2]
                + input[r - 3][c + 3]
                == "XMAS"
            )
        ):
            ans1 += 1

        # NW
        if (
            r - 3 >= 0
            and c - 3 >= 0
            and (
                input[r][c]
                + input[r - 1][c - 1]
                + input[r - 2][c - 2]
                + input[r - 3][c - 3]
                == "XMAS"
            )
        ):
            ans1 += 1

        # SE
        if (
            r + 3 < max_r
            and c + 3 < max_c
            and (
                input[r][c]
                + input[r + 1][c + 1]
                + input[r + 2][c + 2]
                + input[r + 3][c + 3]
                == "XMAS"
            )
        ):
            ans1 += 1

        # SW
        if (
            r + 3 < max_r
            and c - 3 >= 0
            and (
                input[r][c]
                + input[r + 1][c - 1]
                + input[r + 2][c - 2]
                + input[r + 3][c - 3]
                == "XMAS"
            )
        ):
            ans1 += 1

print(ans1)


ans2 = 0
for r in range(max_r):
    for c in range(max_c):
        if input[r][c] != "A":
            continue

        if r + 1 >= max_r or r - 1 < 0 or c + 1 >= max_c or c - 1 < 0:
            continue

        tl = input[r - 1][c - 1]
        tr = input[r - 1][c + 1]
        bl = input[r + 1][c - 1]
        br = input[r + 1][c + 1]

        if not ((tl == "M" and br == "S") or tl == "S" and br == "M"):
            continue

        if not ((tr == "M" and bl == "S") or tr == "S" and bl == "M"):
            continue

        ans2 += 1

print(ans2)

print(f"took={datetime.now() - start}")
