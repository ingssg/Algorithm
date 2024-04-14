import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
cnt = 1


def dfs(graph, start, visited, order):
    global cnt
    visited[start] = True
    order[start] = cnt
    for next in graph[start]:
        if not visited[next]:
            cnt += 1
            dfs(graph, next, visited, order)


def ans():
    global cnt
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    order = [0] * (n + 1)
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    for i in graph:
        i.sort(reverse=True)
    visited[r] = True
    order[r] = cnt
    dfs(graph, r, visited, order)

    for i in order[1:]:
        print(i)


ans()
