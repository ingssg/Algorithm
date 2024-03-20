import sys


def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        temp = power(a, b // 2)
        return (temp * temp) % c
    else:
        return (a * power(a, b - 1)) % c


a, b, c = map(int, sys.stdin.readline().split())

print(power(a, b) % c)
