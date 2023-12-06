import sys

with open(sys.argv[1], 'r') as file:
    avail_time = int(file.readline().replace(' ', '').split(':')[1])
    dist_record = int(file.readline().replace(' ', '').split(':')[1])

count = 0
for hold_time in range(avail_time):
    dist = (avail_time - hold_time) * hold_time
    if dist > dist_record:
        count += 1

print(count)