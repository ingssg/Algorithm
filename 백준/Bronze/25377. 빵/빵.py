import sys
input = sys.stdin.readline


def ans():
    _min = float('inf')

    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        if a <= b:
            _min = min(_min, b)
    if _min == float('inf'):
        print(-1)
        return
    print(_min)


ans()
