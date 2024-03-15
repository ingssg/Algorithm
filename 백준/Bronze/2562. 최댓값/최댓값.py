import sys

data = [int(sys.stdin.readline()) for i in range(9)]

max = data[0]
max_index = 1
for index, i in enumerate(data, start=1):
    if i > max:
        max = i
        max_index = index
print(max)
print(max_index)
