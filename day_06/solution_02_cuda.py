import sys
import numpy as np
from numba import cuda

@cuda.jit
def calculate_counts(avail_time, dist_record, counts):
    tid = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x

    if tid < avail_time:
        dist = (avail_time - tid) * tid
        if dist > dist_record:
            cuda.atomic.add(counts, 0, 1)


with open(sys.argv[1], 'r') as file:
    avail_time = int(file.readline().replace(' ', '').split(':')[1])
    dist_record = int(file.readline().replace(' ', '').split(':')[1])

threads_per_block = 128
blocks = (avail_time + (threads_per_block - 1)) // threads_per_block

counts = cuda.device_array(1, dtype=np.int32)
calculate_counts[blocks, threads_per_block](avail_time, dist_record, counts)

count = counts.copy_to_host()[0]
print(count)