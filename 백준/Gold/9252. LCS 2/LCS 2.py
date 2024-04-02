import sys

input = sys.stdin.readline


def ans():
    a = input().strip()
    b = input().strip()
    dp = [[''] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + a[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    # for row in dp:
    #     print(row)
    print(len(dp[-1][-1]))
    if len(dp[-1][-1]) != 0:
        print(dp[-1][-1])

ans()
