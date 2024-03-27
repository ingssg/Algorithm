import sys

input = sys.stdin.readline


def perms(arr: list) -> list:
    result = []

    def backtrack(current, remaining):
        nonlocal result
        if len(current) == len(arr):
            result.append(current)
            return
        for i in range(len(remaining)):
            backtrack(current + [remaining[i]], remaining[:i] + remaining[i + 1:])

    backtrack([], arr)
    return result


def ans():
    n = int(input())
    nums = list(map(int, input().split()))
    oper = list(map(int, input().split()))

    _max = -1e9
    _min = 1e9

    def dfs(num, idx, add, sub, mul, div):
        nonlocal _max, _min, n, nums
        if idx == n:
            _max = max(_max, num)
            _min = min(_min, num)
            return

        if add > 0:
            dfs(num + nums[idx], idx + 1, add - 1, sub, mul, div)
        if sub > 0:
            dfs(num - nums[idx], idx + 1, add, sub - 1, mul, div)
        if mul > 0:
            dfs(num * nums[idx], idx + 1, add, sub, mul - 1, div)
        if div > 0:
            dfs(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)

    dfs(nums[0], 1, oper[0], oper[1], oper[2], oper[3])

    print(int(_max))
    print(int(_min))

ans()
