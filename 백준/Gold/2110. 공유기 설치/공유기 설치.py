import sys

n, k = map(int, sys.stdin.readline().split())
datas = [int(sys.stdin.readline()) for _ in range(n)]

datas.sort()


def calc_cnt(houses, dist):
    cnt = 1
    cur_house = houses[0]

    for house in houses:
        if house - cur_house >= dist:
            cnt += 1
            cur_house = house
    return cnt


def router(houses, k):
    left = 1
    right = houses[-1] - houses[0]
    result = 0
    while left <= right:
        dist = (left + right) // 2

        if calc_cnt(houses, dist) < k:
            right = dist - 1
        else:
            result = dist
            left = dist + 1

    return result


print(router(datas, k))
