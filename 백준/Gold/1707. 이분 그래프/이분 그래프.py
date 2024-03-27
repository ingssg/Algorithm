import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(graph, start, color, result):
    for g in graph[start]:
        if color[g] == color[start]:
            result.append('NO')
            return
        if color[g] == 0:
            color[g] = - color[start]
            dfs(graph, g, color, result)


def case():
    v, e = map(int, input().split())
    nodes = [[] for _ in range(v + 1)]
    nodes_color = [0 for _ in range(v + 1)]
    result = []
    for _ in range(e):
        start, end = map(int, input().split())
        nodes[start].append(end)
        nodes[end].append(start)
    for i in range(1, v + 1):
        if nodes_color[i] == 0:
            nodes_color[i] = 1
            dfs(nodes, i, nodes_color, result)

    if not result:
        print('YES')
    else:
        print('NO')


def ans():
    k = int(input())
    for _ in range(k):
        case()


ans()
