import sys
import heapq

input = sys.stdin.readline


def ans():
    n = int(input())
    lines = []
    for _ in range(n):
        a, b = map(int, input().split())
        lines.append([min(a, b), max(a, b)])
    d = int(input())
    lines.sort(key=lambda x: (x[1], x[0]))
    que = []
    max_cnt = 0
    for line in lines:
        start, end = line
        heapq.heappush(que, start)
        line_start = end - d
        while que and que[0] < line_start:
            heapq.heappop(que)
        max_cnt = max(max_cnt, len(que))
    print(max_cnt)


ans()
