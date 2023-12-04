import sys

total = 0
file = open(sys.argv[1], 'r')
lines = file.readlines()

cards = [1] * len(lines)

for i, line in enumerate(lines):
    _, numbers, winning_numbers = line.rstrip().translate(str.maketrans(':', '|')).split('| ')
    numbers = set(numbers.split())
    winning_numbers = set(winning_numbers.split())
    matches = len(numbers & winning_numbers)
    
    for j in range(1, matches + 1):
        cards[i + j] += cards[i]
    
file.close()
print(sum(cards))