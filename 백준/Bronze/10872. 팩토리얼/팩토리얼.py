import sys


def factorial(num: int) -> int:
    if num == 0:
        return 1
    return num * factorial(num - 1)


n = int(sys.stdin.readline())

print(factorial(n))
