import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline
result = 0


def dfs(graph, node, visited, dir):
    global result
    for i in range(4):
        go_x = node[0] + dir[i][0]
        go_y = node[1] + dir[i][1]
        if go_x < 0 or go_y < 0 or go_x >= len(graph) or go_y >= len(graph):
            continue
        if not visited[go_x][go_y] and graph[go_x][go_y] != '0':
            result += 1
            visited[go_x][go_y] = True
            dfs(graph, [go_x, go_y], visited, dir)


def ans():
    global result
    n = int(input())
    graph = []
    for i in range(n):
        a = input().strip()
        graph.append(list(a))
    visited = [[False for _ in range(n)] for _ in range(n)]
    dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    cnt = 0
    rst = []
    for row in range(n):
        for col in range(n):
            if not visited[row][col] and graph[row][col] != '0':
                visited[row][col] = True
                dfs(graph, [row, col], visited, dir)
                rst.append(result)
                result = 0
                cnt += 1

    print(cnt)
    rst.sort()
    for r in rst:
        print(r + 1)


ans()
