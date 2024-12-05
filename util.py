import re


def row_to_col(matrix: list[str], i: int):
    return "".join(row[i] for row in matrix)


def rows_to_cols(matrix: list[str]) -> list[str]:
    return [row_to_col(matrix, i) for i in range(len(matrix[0]))]


def ints(s: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", s)))
