import sys

input = sys.stdin.readline


def ans():
    dp = [0 for _ in range(11)]
    t = int(input())
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 11):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    for _ in range(t):
        num = int(input())
        print(dp[num])


ans()
