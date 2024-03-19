import sys

num = int(sys.stdin.readline())

lst = [0] * 10001

for _ in range(num):
    lst[int(sys.stdin.readline())] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)
