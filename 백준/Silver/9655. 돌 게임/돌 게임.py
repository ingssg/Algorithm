import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    d = [0 for _ in range(n + 1)]

    if n == 1:
        print('SK')
        return
    if n == 2:
        print('CY')
        return

    d[1], d[2], d[3] = 1, 2, 1

    for i in range(4, n + 1):
        d[i] = max(d[i - 1], d[i - 3]) + 1

    if d[n] % 2 == 0:
        print('CY')
    else:
        print('SK')


ans()
