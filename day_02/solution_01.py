import sys

colors = {'red': 12, 'green': 13, 'blue': 14}
id_sum = 0

with open(sys.argv[1], 'r') as file:
    for line in file:
        prefix, draws = line.strip().split(':')
        game_id = prefix.split()[1]
    
        for game in draws.strip().split(';'):
            for draw in game.split(','):
                amount, color = draw.split()
                if int(amount) > colors[color]:
                    break
            else:
                continue
            break
        else:
            id_sum += int(game_id)

print(id_sum)

