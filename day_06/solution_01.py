import sys

with open(sys.argv[1], 'r') as file:
    avail_time = list(map(int, file.readline().split(':')[1].split()))
    dist_record = list(map(int, file.readline().split(':')[1].split()))


total = 1
for time, record in zip(avail_time, dist_record):
    count = 0
    for hold_time in range(time):
        dist = (time - hold_time) * hold_time
        if dist > record:
            count += 1
    total *= count

print(total)