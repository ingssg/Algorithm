import sys
from collections import deque

input = sys.stdin.readline


def ans():
    n, m = map(int, input().split())
    hutgan = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        hutgan[a].append(b)
        hutgan[b].append(a)

    visited = [False for _ in range(n + 1)]
    lists = deque()
    lists.append(1)
    visited[1] = True
    distance = [0 for _ in range(n + 1)]
    while lists:
        start = lists.popleft()
        for next in hutgan[start]:
            if not visited[next]:
                distance[next] = distance[start] + 1
                visited[next] = True
                lists.append(next)

    _max = max(distance)
    _max_idx = distance.index(_max)
    cnt = 0
    for i in range(1, n + 1):
        if distance[i] == _max:
            cnt += 1
    print(_max_idx, _max, cnt)


ans()
