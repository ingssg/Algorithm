import sys
import heapq

input = sys.stdin.readline


def ans(start_v):
    q = []
    distance[start_v] = 0
    heapq.heappush(q, (0, start_v))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node in graph[now]:
            cost = dist + next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [int(1e9) for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
start, end = map(int, input().split())

ans(start)
print(distance[end])
