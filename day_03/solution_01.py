import sys

def parse_textfile(path=sys.argv[1]):
    matrix = []
    with open(path, 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix


def check_bounds(i, j):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
        return True
    return False


def check_neighborhood(i, j):
    neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for n_i, n_j in neighbors:
        y, x = i + n_i, j + n_j
        if check_bounds(y, x) and matrix[y][x] != '.' and not matrix[y][x].isdigit():
            return True
    return False


def evaluate_number(i, j):
    symbol_found = False
    number = ""

    while check_bounds(i, j) and matrix[i][j].isdigit():
        number += matrix[i][j]
        if not symbol_found:
            symbol_found = check_neighborhood(i, j)
        j += 1
    return (int(number), j) if symbol_found else (0, j)


matrix = parse_textfile()
n, m = len(matrix), len(matrix[0])
total = 0

for i in range(n):
    j = 0
    while j < m:
        if matrix[i][j].isdigit():
            num, next_j = evaluate_number(i, j)
            total += num
            j = next_j
        else:
            j += 1

print(total)


