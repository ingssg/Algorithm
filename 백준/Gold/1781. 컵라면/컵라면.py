import sys
import heapq

input = sys.stdin.readline


def ans():
    n = int(input())
    ramen = [list(map(int, input().split())) for _ in range(n)]
    ramen.sort()
    heap = []
    for r in ramen:
        heapq.heappush(heap, r[1])
        if r[0] < len(heap):
            heapq.heappop(heap)

    print(sum(heap))


ans()
