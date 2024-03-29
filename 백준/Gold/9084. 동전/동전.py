import sys

input = sys.stdin.readline


def ans():
    k = int(input())
    for _ in range(k):
        n = int(input())
        dp = [0 for i in range(10001)]
        dp[0] = 1
        coins = list(map(int, input().split()))
        case = int(input())

        for coin in coins:
            for i in range(1, case + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]

        print(dp[case])


ans()
