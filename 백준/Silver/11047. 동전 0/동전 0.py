import sys

input = sys.stdin.readline

def ans():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort(reverse=True)
    cnt = 0
    for i in range(n):
        if coins[i] > k:
            continue
        cnt += k // coins[i]
        k %= coins[i]
    print(cnt)

ans()
