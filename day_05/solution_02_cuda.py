import sys
import numpy as np
from numba import cuda

@cuda.jit
def calculate_minimum(offset, local_min, map1, map2, map3, map4, map5, map6, map7):
    tid = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x

    current = offset + tid
    for mapping in [map1, map2, map3, map4, map5, map6, map7]:
        for curr in mapping:
            dest, source, span = curr
            if source <= current < (source + span):
                current = dest + (current - source)
                break
    cuda.atomic.min(local_min, 0, current)


with open(sys.argv[1], 'r') as file:
    content = file.read()

seeds, *maps = content.split("\n\n")
seeds = np.array(list(map(int, seeds.split(':')[1].split())))

for i, section in enumerate(maps):
    section = section.split(":\n")[1]
    maps[i] = cuda.to_device([list(map(int, line.split())) for line in section.split('\n')])

minimum = np.inf
for i in range(0, len(seeds), 2):
    offset, span = seeds[i], seeds[i + 1]
    
    threads_per_block = 128
    blocks = (span + (threads_per_block - 1)) // threads_per_block

    local_min = cuda.to_device([np.inf])
    calculate_minimum[blocks, threads_per_block](offset, local_min, *maps)
    minimum = min(minimum, local_min.copy_to_host())

print(int(minimum))