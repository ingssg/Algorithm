# 특정 거리의 도시 찾기
import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def ans():
    n, m, k, x = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
    visited = [False for _ in range(n + 1)]
    que = deque()
    que.append((x, 0))
    ans = []
    visited[x] = True

    while que:
        pos, dist = que.popleft()
        if dist == k:
            ans.append(pos)

        for p in graph[pos]:
            if not visited[p]:
                visited[p] = True
                que.append((p, dist + 1))

    if not ans:
        print(-1)
        return
    ans.sort()
    for a in ans:
        print(a)


ans()
