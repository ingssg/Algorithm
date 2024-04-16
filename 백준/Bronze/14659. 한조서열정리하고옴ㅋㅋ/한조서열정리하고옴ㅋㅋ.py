import sys

input = sys.stdin.readline

def ans2():    # 그냥 cnt 사용 
    n = int(input())
    bongs = list(map(int, input().split()))
    res = 0
    cnt = 0
    cur_max = bongs[0]
    for i in range(1, n):
        if bongs[i] < cur_max:
            cnt += 1
        else:
            cur_max = bongs[i]
            res = max(cnt, res)
            cnt = 0
    res = max(cnt, res)
    print(res)


ans2()