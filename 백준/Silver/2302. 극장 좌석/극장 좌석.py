import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    m = int(input())
    sheet = [int(input()) for _ in range(m)]
    dp = [0] * (n + 1)
    if n == 1:
        print(1)
        return
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # print(dp)
    tmp = []
    if sheet:
        tmp.append(sheet[0])
        for i in range(len(sheet)-1):
            tmp.append(sheet[i + 1] - sheet[i])
        tmp.append(n - sheet[-1] + 1)
    # print(tmp)

    if m == 0:
        print(dp[n])
        return
    ans_ = 1
    for t in tmp:
        ans_ *= dp[t-1]
    print(ans_)


ans()
