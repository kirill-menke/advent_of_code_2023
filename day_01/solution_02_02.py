import sys

numbers_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

total = 0
with open(sys.argv[1], 'r') as file:
    numbers = []

    while line := file.readline():
        for i, char in enumerate(line):
            if char.isnumeric():
                numbers.append(char)
            else:
                for num in numbers_map.keys():
                    if line[i:].startswith(num):
                        numbers.append(str(numbers_map[num]))

        total += int(numbers[0] + numbers[-1])
        numbers.clear()
    
print(total)