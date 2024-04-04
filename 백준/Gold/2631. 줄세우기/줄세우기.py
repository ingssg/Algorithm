import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    child = [int(input()) for _ in range(n)]
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if child[i] < child[j]:
                dp[j] = max(dp[j], dp[i] + 1)

    print(n - max(dp))


ans()
