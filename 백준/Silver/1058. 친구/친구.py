import sys
from collections import deque

input = sys.stdin.readline


def ans():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        line = list(input().strip())
        for j in range(n):
            if line[j] == 'Y':
                graph[i].append(j + 1)
    max_f = 0

    for i in range(1, n + 1):
        isvisited = [False for _ in range(n + 1)]
        isvisited[i] = True
        que = deque([i])
        tmp_max = 0
        depth = [0 for _ in range(n + 1)]
        while que:
            start = que.popleft()
            for end in graph[start]:
                if not isvisited[end]:
                    isvisited[end] = True
                    depth[end] = depth[start] + 1
                    que.append(end)
                    if depth[end] <= 2:
                        tmp_max += 1
                    else:
                        break

        max_f = max(tmp_max, max_f)

    print(max_f)


ans()
