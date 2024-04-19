import sys

input = sys.stdin.readline


def ans():
    n, k = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(n)]
    countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
    idx = 1
    rating = 1
    diff = 0

    if countries[0][0] == 1 and k == 1:
        print(1)
        return
    for c in countries[idx:]:
        last_g, last_s, last_b = countries[idx-1][1:]
        cur_g, cur_s, cur_b = c[1:]
        if cur_g == last_g and cur_s == last_s and cur_b == last_b:
            idx += 1
            diff += 1
            if c[0] == k:
                break
            continue
        rating += 1
        idx += 1
        if diff != 0:
            rating += diff
            diff = 0
        if c[0] == k:
            break

    print(rating)


ans()
