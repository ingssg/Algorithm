n, k = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]
memo = {}


def top_down(n, k):
    if n == 0 or k == 0:
        return 0
    if (n, k) in memo:
        return memo[(n, k)]
    w, v = things[n - 1]
    if k < w:
        result = top_down(n - 1, k)
    else:
        result = max(top_down(n - 1, k), top_down(n - 1, k - w) + v)
    memo[(n, k)] = result
    return result


print(top_down(n, k))
