import sys

input = sys.stdin.readline

def ans():
    a, k = map(int, input().split())
    dp = [0 for _ in range(k+1)]

    for i in range(a+1, k+1):
        dp[i] = dp[i-1] + 1

    for i in range(2*a, k+1):
        if i % 2 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
        else:
            dp[i] = min(dp[i//2] + 2, dp[i-1] + 1)

    print(dp[k])


ans()