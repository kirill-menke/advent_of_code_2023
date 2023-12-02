import sys
import math
from collections import defaultdict

total = 0

with open(sys.argv[1], 'r') as file:
    for line in file:
        draws = line.strip().split(':')[1]
        colors = defaultdict(int)

        for game in draws.strip().split(';'):
            for draw in game.split(','):
                amount, color = draw.split()
                if int(amount) > colors[color]:
                    colors[color] = int(amount)
        power = math.prod(colors.values())
        total += power
        

print(total)