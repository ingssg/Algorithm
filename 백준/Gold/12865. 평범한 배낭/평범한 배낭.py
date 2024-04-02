import sys

input = sys.stdin.readline


def ans():
    n, k = map(int, input().split())
    things = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (k + 1)
    for w, v in things:
        for i in range(k, w-1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    print(dp[-1])


ans()
