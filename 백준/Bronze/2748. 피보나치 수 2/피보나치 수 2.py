import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    d = [0 for _ in range(n + 1)]
    if n == 1:
        print(1)
        return
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    print(d[n])


ans()
