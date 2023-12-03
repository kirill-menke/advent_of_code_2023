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


def get_gear_ratio(i, j):
    neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    numbers = set()

    for n_i, n_j in neighbors:
        y, x = i + n_i, j + n_j
        if check_bounds(y, x) and number_matrix[y][x] is not None:
            numbers.add(number_matrix[y][x])
    
    return numbers.pop()[0] * numbers.pop()[0] if len(numbers) == 2 else 0


matrix = parse_textfile()
n, m = len(matrix), len(matrix[0])
number_matrix = [[None] * m for _ in range(n)]

for i in range(n):
    digits = []
    start_idx = None
    for j in range(m):
        if matrix[i][j].isdigit():
            if not digits:
                start_idx = j
            digits.append(matrix[i][j])
        elif digits:
            number_matrix[i][start_idx: j] = [(int(''.join(digits)), start_idx)] * (j - start_idx)
            digits.clear()
    if digits:
        number_matrix[i][start_idx: m] = [(int(''.join(digits)), start_idx)] * (m - start_idx)


total = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '*':
            total += get_gear_ratio(i, j)

print(total)