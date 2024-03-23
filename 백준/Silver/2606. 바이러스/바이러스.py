import sys

input = sys.stdin.readline


def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def ans():
    n = int(input())  # 정점의 수
    m = int(input())  # 간선의 수
    visited = [False] * (n + 1)
    cnt = 0
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(graph, 1, visited)

    for isvisited in visited:
        if isvisited == True:
            cnt += 1

    print(cnt - 1)


ans()
