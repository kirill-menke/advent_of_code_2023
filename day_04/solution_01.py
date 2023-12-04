import sys

total = 0
file = open(sys.argv[1], 'r')

for i, line in enumerate(file):
    _, numbers, winning_numbers = line.rstrip().translate(str.maketrans(':', '|')).split('| ')
    numbers = set(numbers.split())
    winning_numbers = set(winning_numbers.split())
    matches = len(numbers & winning_numbers)
    points = 2 ** (matches - 1) if matches else 0
    total += points

file.close()

print(total)