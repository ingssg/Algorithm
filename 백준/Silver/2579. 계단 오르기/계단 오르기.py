import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    dp = [[0, 0, 0] for _ in range(n + 2)]  # [i, j] i번째 계단에 올랐을 때 연속해서 오른 계단의 수 j
    stairs = [int(input()) for _ in range(n)]

    if n == 1:
        print(stairs[0])
        return
    if n == 2:
        print(stairs[0] + stairs[1])
        return

    dp[0][1], dp[0][2] = stairs[0], 0
    dp[1][1], dp[1][2] = stairs[1], stairs[0] + stairs[1]

    for i in range(2, n):
        dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + stairs[i]
        dp[i][2] = dp[i - 1][1] + stairs[i]
        dp[i][0] = max(dp[i][1], dp[i][2])
    print(dp[n - 1][0])


ans()
