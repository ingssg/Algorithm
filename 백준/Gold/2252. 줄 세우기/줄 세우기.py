import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def ans():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    indegree = [0 for _ in range(n + 1)]
    que = deque()
    visited = [False for _ in range(n + 1)]

    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        indegree[end] += 1

    for i in range(1, n + 1):
        if indegree[i] == 0:
            visited[i] = True
            que.append(i)

    while que:
        node = que.popleft()
        print(node, end=" ")
        for h in graph[node]:
            indegree[h] -= 1
            if not visited[h] and indegree[h] == 0:
                visited[h] = True
                que.append(h)


ans()
