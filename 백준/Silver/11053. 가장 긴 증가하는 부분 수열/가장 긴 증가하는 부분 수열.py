import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    dp = [1 for _ in range(n + 1)]
    num = list(map(int, input().split()))
    for i in range(1, n):
        for j in range(i):
            if num[j] < num[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


ans()
