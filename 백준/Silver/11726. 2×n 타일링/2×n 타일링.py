import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    if n == 1:
        print(1)
        return
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    print(dp[n])


ans()
