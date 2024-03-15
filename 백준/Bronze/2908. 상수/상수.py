import sys

a, b = map(str, sys.stdin.readline().split())
print(max(a[::-1], b[::-1]))
