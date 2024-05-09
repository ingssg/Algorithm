import sys

input = sys.stdin.readline


def ans():
    t = int(input())
    for _ in range(t):
        datas = list(map(int, input().split()))
        dist_pow = (datas[0] - datas[3]) ** 2 + (datas[1] - datas[4]) ** 2
        r1, r2 = datas[2], datas[5]
        if dist_pow == 0 and r1 == r2:
            print(-1)
        elif dist_pow == (r1-r2)**2 or dist_pow == (r1+r2)**2:
            print(1)
        elif (r1-r2)**2 < dist_pow < (r1+r2)**2:
            print(2)
        else:
            print(0)


ans()
