import sys


def tsp_perm(arr, n):
    min_cost = float('inf')
    def backtrack(current, remaining, current_cost):
        nonlocal min_cost
        start = 0
        cost = 0
        if len(current) == n:
            for i in current:
                cost += arr[start][i]
                start = i
            if arr[start][0] == 0:
                cost += 999999
            cost += arr[start][0]
            return cost
        else:
            for i in range(len(remaining)):
                next_cost = current_cost + arr[current[-1]][remaining[i]]
                if arr[current[-1]][remaining[i]] != 0 and next_cost < min_cost:
                    sum_cost = backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:], next_cost)
                    min_cost = min(min_cost, sum_cost)
            return min_cost
    min_cost = backtrack([0], list(range(1, n)), 0)
    return min_cost


n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

print(tsp_perm(data, n))
