# 소트마스터 배지훈의 후계자
# https://www.acmicpc.net/problem/20551

import sys

input = sys.stdin.readline

def ans():
    n, m = map(int, input().strip().split())

    data = [int(input().strip()) for _ in range(n)]
    data.sort()

    idx_lst = {}
    # print(data)
    for idx, d in enumerate(data):
        if d in idx_lst:
            continue
        idx_lst[d] = [1, idx]
    # print(idx_lst)

    for a in range(m):
        q = int(input())
        if q in idx_lst:
            print(idx_lst[q][1])
        else:
            print(-1)





    # for a in range(m):
    #     q = int(input())
    #     left = 0
    #     right = len(data)-1
    #     while True:
    #         mid = (left + right) // 2
    #         if data[mid] == q:
    #             if mid == left:
    #                 print(mid)
    #                 break
    #             else:
    #                 left = mid
    #         elif data[mid] < q:
    #             left = mid + 1
    #         elif data[mid] > q:
    #             right = mid - 1
    #         if left > right:
    #             print(-1)
    #             break

        # if q in data:
        #     print(data.index(q))
        # else:
        #     print(-1)


ans()

