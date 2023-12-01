import sys

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

root = {}
for num, integer in numbers.items():
    current = root
    for char in num:
        if char not in current:
            current[char] = {}
        current = current[char]
    current['$'] = str(integer)

total = 0
with open(sys.argv[1], 'r') as file:
    numbers = []
    while line := file.readline():
        current = root
        for char in line:
            if char.isnumeric():
                numbers.append(char)
                current = root
            elif char in current:
                current = current[char]
                if '$' in current:
                    numbers.append(current['$'])
                    current = root
                if char in current:
                    current = root[char]
            elif char in root:
                current = root[char]
            else:
                current = root
                
        total += int(numbers[0] + numbers[-1])
        numbers.clear()
    
print(total)