import sys

input = sys.stdin.readline


def ans():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        cnt = 0
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                x = ((a * a) + (b * b) + m)
                y = a * b
                if x % y == 0:
                    cnt += 1
        print(cnt)


ans()
