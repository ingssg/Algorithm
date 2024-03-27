import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
cnt = 0


def dfs(graph, start, visited, status):
    global cnt
    for g in graph[start]:
        if not visited[g]:
            visited[g] = True
            if status[g] == 1:
                cnt += 1
            else:
                dfs(graph, g, visited, status)


def ans():
    n = int(input())
    status = [-1]
    a = list(input().strip())
    ans = 0
    for i in a:
        status.append(int(i))
    route = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        s, e = map(int, input().split())
        route[s].append(e)
        route[e].append(s)
        if status[s] == 1 and status[e] == 1:
            ans += 2
    visited = [False for _ in range(n + 1)]

    for i in range(1, n + 1):
        global cnt
        cnt = 0
        if status[i] == 0:  # 흰 노드부터 dfs
            visited[i] = True
            dfs(route, i, visited, status)
            ans += cnt * (cnt - 1)
    print(ans)


ans()
