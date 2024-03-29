import sys

input = sys.stdin.readline

def ans():
    n = int(input())
    r = [0]
    g = [0]
    b = [0]
    dp = [[0, 0, 0] for _ in range(n+1)]
    for _ in range(n):
        red, green, blue = map(int, input().split())
        r.append(red)
        g.append(green)
        b.append(blue)
    dp[1][0] = r[1]
    dp[1][1] = g[1]
    dp[1][2] = b[1]
    for i in range(2, n+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r[i]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g[i]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b[i]
    print(min(dp[n][0], dp[n][1], dp[n][2]))


ans()
