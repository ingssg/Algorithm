import sys
from collections import deque

input = sys.stdin.readline


def ans():
    n, k = map(int, input().split())
    que = deque()
    ans_list = []
    for i in range(1, n+1):
        que.append(str(i))
    while len(que) > 1:
        for _ in range(k-1):
            que.append(que.popleft())
        ans_list.append(que.popleft())
    ans_list.append(que.pop())
    print(f'<{", ".join(ans_list)}>')


ans()
