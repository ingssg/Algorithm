import sys

n, k = map(int, sys.stdin.readline().split())
datas = [int(sys.stdin.readline()) for _ in range(n)]

def heos(arr, k):
    left = min(arr)
    right = left + k
    result = 0

    while left <= right:
        center = (left + right) // 2
        _sum = 0
        for i in arr:
            if center > i:
                _sum += center - i
        if _sum <= k:
            result = center
            left = center + 1
        else:
            right = center - 1

    return result


print(heos(datas, k))
