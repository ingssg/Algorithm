import sys

input = sys.stdin.readline


def ans():
    t = int(input())
    k = int(input())
    coins = [list(map(int, input().split())) for _ in range(k)]
    dp = [0] * (t + 1)
    dp[0] = 1
    for coin in coins:
        v, cnt = coin
        for i in range(t, v - 1, -1):
            for c in range(1, cnt + 1):
                if v * c <= i:
                    dp[i] += dp[i - (v * c)]    
    print(dp[-1])


ans()
