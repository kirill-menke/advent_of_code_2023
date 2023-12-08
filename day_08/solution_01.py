import sys
import itertools

with open(sys.argv[1], 'r') as file:
    directions, maps = file.read().split('\n\n')
    graph = {}
    for line in maps.split('\n'):
        src, dst = line.split(" = ")
        dst_left, dst_right = dst.strip('()').split(', ')
        graph[src] = {'L': dst_left, 'R': dst_right}

node = "AAA"
for i, dir in enumerate(itertools.cycle(directions)):
    if node == "ZZZ":
        break
    node = graph[node][dir]

print(i)
