import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(g, start, visited):
    visited[start] = True  # 방문시 체크
    for v in g[start]:  # 해당 정점에서 갈 수 있는 곳 체크
        if not visited[v]:  # 안들른 곳이면
            dfs(g, v, visited)  # 들려라


def ans():
    n, m = map(int, input().split())  # 정점의 개수, 간선의 개수
    count = 0  # 연결 요소 수 초기화
    visited = [False] * (n + 1)  # 정점 방문 리스트 초기화
    graph = [[] for _ in range(n + 1)]  # 정점당 갈 수 있는 곳 저장 , 1번 인덱스부터 저장하기 위해 한칸 더 받음
    for _ in range(m):
        u, v = map(int, input().split())  # 간선정보 : 출발지 , 도착지
        graph[u].append(v)  # 출발지점에서 갈 수 있는 정점 저장
        graph[v].append(u)  # 도착지점에서 갈 수 있는 정점 저장

    for i in range(1, n + 1):  # 1번 인덱스부터 저장했으니까
        if not visited[i]:  # 안 들른 곳 있으면
            dfs(graph, i, visited)  # 들려라
            count += 1  # 다 들렸으면 + 1
    return count


print(ans())
