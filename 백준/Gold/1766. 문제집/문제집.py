# 문제집
import sys
import heapq

input = sys.stdin.readline


def ans():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    heap = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    while heap:
        node = heapq.heappop(heap)
        print(node, end=" ")
        for g in graph[node]:
            indegree[g] -= 1
            if indegree[g] == 0:
                heapq.heappush(heap, g)


ans()
