import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]

# a b 가중치

trees = {}
for info in infos:
    try:
        trees[info[0]] += [info[1:]]
    except:
        trees[info[0]] = [info[1:]]
    try:
        trees[info[1]] += [[info[0]] + [info[2]]]
    except:
        trees[info[1]] = [[info[0]] + [info[2]]]


def prim(graph):
    is_visited = [False] * len(graph)
    start = 0
    is_visited[start] = True
    min_heap = []  # 간선 저장
    mst = []  # 최소 스패닝 트리

    for end, weight in graph[1]:
        heapq.heappush(min_heap, (weight, end))

    while len(mst) < v - 1:
        weight, neighbor = heapq.heappop(min_heap)
        if is_visited[neighbor - 1]:
            continue

        mst.append(weight)
        is_visited[neighbor - 1] = True
        for end, weight in graph[neighbor]:
            if not is_visited[end - 1]:
                heapq.heappush(min_heap, (weight, end))

    return sum(mst)


print(prim(trees))
