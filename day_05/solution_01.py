import sys

with open(sys.argv[1], 'r') as file:
    content = file.read()

seeds, *maps = content.split("\n\n")
seeds = list(map(int, seeds.split(':')[1].split()))

for i, section in enumerate(maps):
    section = section.split(":\n")[1]
    maps[i] = [list(map(int, line.split())) for line in section.split('\n')]

for mapping in maps:
    for i, seed in enumerate(seeds):
        for curr in mapping:
            dest, source, span = curr
            if source <= seed < (source + span):
                seeds[i] = dest + (seed - source)

print(min(seeds))