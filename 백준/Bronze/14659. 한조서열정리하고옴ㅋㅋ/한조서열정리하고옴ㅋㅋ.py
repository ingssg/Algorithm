import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    bongs = list(map(int, input().split()))
    stack = []
    res = 0
    max_ = bongs[0]
    for i in range(1, n):
        if bongs[i] < max_:
            stack.append(bongs[i])
        else:
            max_ = bongs[i]
            res = max(res, len(stack))
            stack.clear()

    res = max(res, len(stack))
    print(res)


ans()
