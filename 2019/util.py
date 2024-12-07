import re

# NORTH EAST SOUTH WEST
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def row_to_col(grid: list[str], i: int):
    return "".join(row[i] for row in grid)


def rows_to_cols(grid: list[str]) -> list[str]:
    return [row_to_col(grid, i) for i in range(len(grid[0]))]


def replace_char(grid: list[str], r: int, c: int, ch: str):
    new_r = list(grid[r])
    new_r[c] = ch
    grid[r] = "".join(new_r)


def ints(s: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", s)))
