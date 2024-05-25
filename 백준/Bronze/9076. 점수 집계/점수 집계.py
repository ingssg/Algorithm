import sys
from collections import deque

input = sys.stdin.readline


def ans():
    t = int(input())
    for _ in range(t):
        scores = list(map(int, input().split()))
        scores.sort()
        que = deque(scores)
        que.popleft()
        que.pop()
        if (que[-1] - que[0]) >= 4:
            print("KIN")
        else:
            print(sum(que))


ans()
