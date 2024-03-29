import sys

input = sys.stdin.readline


def ans():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    d = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i] = d[i - 1] + nums[i-1]
    for _ in range(m):
        i, j = map(int, input().split())
        print(d[j] - d[i - 1])


ans()
