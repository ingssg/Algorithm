# 미로
import sys
from collections import deque

input = sys.stdin.readline


def ans():
    row, column = map(int, input().split())
    graph = []
    visited = [[False] * column for _ in range(row)]
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in range(row):
        r = list(input().strip())
        graph.append(r)

    que = deque([[0, 0, 1]])
    visited[0][0] = True
    cnt = 0
    while que:
        _row, _column, cnt = que.popleft()
        if _row == row-1 and _column == column-1:
            break
        for i in range(4):
            nrow = _row + dir[i][0]
            ncol = _column + dir[i][1]
            if nrow < 0 or ncol < 0 or nrow >= row or ncol >= column:
                continue
            if not visited[nrow][ncol] and graph[nrow][ncol] == '1':
                que.append([nrow, ncol, cnt + 1])
                visited[nrow][ncol] = True
    print(cnt)


ans()
