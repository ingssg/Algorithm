import sys
from collections import deque

input = sys.stdin.readline


def ans():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dfs_visited = [False] * (n + 1)
    bfs_visited = [False] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for g in graph:
        g.sort()

    dfs(graph, v, dfs_visited)
    print()
    bfs(graph, v, bfs_visited)


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        first = queue.popleft()
        print(first, end=" ")
        for x in graph[first]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True


ans()
