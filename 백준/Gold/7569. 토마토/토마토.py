import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, queue: deque, dir, m, n, h):
    while len(queue) > 0:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dir[i % 6][0], y + dir[i % 6][1], z + dir[i % 6][2]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append((nz, nx, ny))


def ans():
    m, n, h = map(int, input().split())
    graph = []
    dir = [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    for _ in range(h):
        floor = [list(map(int, input().split())) for _ in range(n)]
        graph.append(floor)
    tomato = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    tomato.append((i, j, k))

    bfs(graph, tomato, dir, m, n, h)


    max_day = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:  # 안익은 토마토가 있으면 안돼
                    return -1
                max_day = max(max_day, graph[i][j][k])

    if max_day == 1:
        return 0
    else:
        return max_day - 1    ## 처음에 1로 시작하니까


print(ans())
