import sys

input = sys.stdin.readline

def ans():
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 1
        sawons = [list(map(int, input().split())) for _ in range(n)]
        sawons.sort()
        _max = sawons[0][1]
        for i in range(1, n):
            if sawons[i][1] < _max:
                cnt += 1
                _max = sawons[i][1]
        print(cnt)


ans()
