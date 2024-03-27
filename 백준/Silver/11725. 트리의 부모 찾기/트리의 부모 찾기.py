import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict

input = sys.stdin.readline


def dfs(graph, start, visited, parents):
    for node in graph[start]:
        if not visited[node]:
            visited[node] = True
            parents[node] = start
            dfs(graph, node, visited, parents)


def ans():
    n = int(input())
    nodes = defaultdict(list)
    for _ in range(n - 1):
        start, end = map(int, input().split())
        nodes[start].append(end)
        nodes[end].append(start)
    parents = [0 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    visited[1] = True
    dfs(nodes, 1, visited, parents)

    for p in parents[2:]:
        print(p)


ans()
