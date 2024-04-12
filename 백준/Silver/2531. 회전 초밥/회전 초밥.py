import sys
from collections import deque

input = sys.stdin.readline


def ans():
    # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
    n, d, k, c = map(int, input().split())
    chobabs = [int(input()) for _ in range(n)]
    select = deque()

    # print(n, d, k, c)
    # print(chobabs)
    # 쿠폰 선택하지 않는 경우 + 쿠폰
    max_set = 0
    for i in range(n):
        select_set = set()
        for j in range(i, i + k):
            select_set.add(chobabs[j % n])
        if c not in select_set:
            select_set.add(-1)
        max_set = max(max_set, len(select_set))
    print(max_set)


ans()
