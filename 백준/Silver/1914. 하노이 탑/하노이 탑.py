import sys


def hanoi(n, start, end):
    if n == 0:
        return
    else:
        hanoi(n-1, start, 6-start-end)
        print(start, end)
        hanoi(n-1, 6-start-end, end)


num = int(sys.stdin.readline())

print(2 ** num - 1)
if num <= 20:
    hanoi(num, 1, 3)
