import sys

total = 0
with open(sys.argv[1], 'r') as file:
    numbers = []
    while line := file.readline():
        for char in line:
            if char.isnumeric():
                numbers.append(char)
        total += int(numbers[0] + numbers[-1])
        numbers.clear()

print(total)