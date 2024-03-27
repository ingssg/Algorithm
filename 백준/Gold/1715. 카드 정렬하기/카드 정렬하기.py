import sys
import heapq

input = sys.stdin.readline


def ans():
    n = int(input())
    card = []
    for _ in range(n):
        heapq.heappush(card, int(input()))
    cnt = 0
    for _ in range(n-1):
        a = heapq.heappop(card)
        b = heapq.heappop(card)
        cnt += (a+b)
        heapq.heappush(card, a+b)

    print(cnt)


ans()
