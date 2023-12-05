import sys

with open(sys.argv[1], 'r') as file:
    content = file.read()

seeds, *maps = content.split("\n\n")
seeds = list(map(int, seeds.split(':')[1].split()))

for i, section in enumerate(maps):
    section = section.split(":\n")[1]
    maps[i] = [list(map(int, line.split())) for line in section.split('\n')]

minimum = float("inf")
for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
        current = seed
        for mapping in maps:
            for curr in mapping:
                dest, source, span = curr
                if source <= current < (source + span):
                    current = dest + (current - source)
                    break
        minimum = min(minimum, current)

print(minimum)