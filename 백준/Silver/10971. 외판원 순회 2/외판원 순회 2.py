import sys


def tsp_perm(arr, n):
    min_cost = float('inf')
    def backtrack(current, remaining, current_cost):
        nonlocal min_cost  # 외부 함수의 로컬 변수를 가져옴
        start = 0
        cost = 0
        if len(current) == n: # 만든 순열의 크기가 주어진 크기와 같음 >> 순열 완성 시
            for i in current:
                cost += arr[start][i]   # 돌면서 더함
                start = i
            if arr[start][0] == 0:  # 만약 출발지로 돌아갈 길이 없다면
                cost += 999999
            cost += arr[start][0]
            return cost
        else:
            for i in range(len(remaining)):
                next_cost = current_cost + arr[current[-1]][remaining[i]] # 현재 비용에 가야할 곳의 비용을 더해줌
                if arr[current[-1]][remaining[i]] != 0 and next_cost < min_cost: # 갈 수 있는 곳이고, 비용을 더했을 때 최소보다 작다면
                    sum_cost = backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:], next_cost) # 출발
                    min_cost = min(min_cost, sum_cost)
            return min_cost
    min_cost = backtrack([0], list(range(1, n)), 0) # 0번부터 출발
    return min_cost


n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

print(tsp_perm(data, n))
