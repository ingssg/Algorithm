import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def ans():
    n = int(input())  # 도시의 개수
    m = int(input())  # 도로의 개수
    cities = defaultdict(list)
    indegree = [0] * (n + 1)    # 노드별 진입 차수
    dist = [0] * (n + 1) # 노드별 가중치 합

    last_update = [[]] * (n + 1)    # 도시에 가장 큰 가중치를 가지고 왔던 노드

    for i in range(m):
        fr, to, weight = tuple(map(int, input().split()))
        indegree[to] += 1
        cities[fr].append((to, weight))

    start, end = map(int, input().split())

    queue = deque([start])

    # 최대치 위상정렬
    while queue:
        cur = queue.popleft()
        for next, weight in cities[cur]:
            indegree[next] -= 1

            cur_dist = dist[cur] + weight

            # 최대 거리 갱신하면 last_update에 최대 값 준 도시 갱신
            if cur_dist > dist[next]:
                dist[next] = cur_dist
                last_update[next] = [cur]
            elif cur_dist == dist[next]:    # 거리가 같으면 추가
                last_update[next].append(cur)

            if indegree[next] == 0:     # 진입 노드가 0이면 큐에 추가
                queue.append(next)

    # 역추적 해서 개수 찾기

    queue = deque([end])
    ans = 0
    visited = [False] * (n + 1)
    visited[end] = True
    ans += len(last_update[end])
    while queue:
        cur = queue.popleft()

        for next in last_update[cur]:
            if not visited[next]:
                visited[next] = True
                ans += len(last_update[next])
                queue.append(next)

    print(dist[end])
    print(ans)


ans()
