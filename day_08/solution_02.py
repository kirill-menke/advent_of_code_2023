import sys
import math
import itertools

def calculate_steps(node):
    for i, dir in enumerate(itertools.cycle(directions)):
        if node.endswith('Z'):
            return i
        node = graph[node][dir]

with open(sys.argv[1], 'r') as file:
    directions, maps = file.read().split('\n\n')
    graph = {}
    for line in maps.split('\n'):
        src, dst = line.split(" = ")
        dst_left, dst_right = dst.strip('()').split(', ')
        graph[src] = {'L': dst_left, 'R': dst_right}

steps = [calculate_steps(node) for node in graph.keys() if node.endswith('A')]
lcm = math.lcm(*steps)

print(lcm)