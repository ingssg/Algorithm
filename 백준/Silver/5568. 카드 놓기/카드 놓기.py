import sys
import itertools

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = [sys.stdin.readline().strip() for _ in range(n)]

result = set()
perms = itertools.permutations(cards, k)

for perm in perms:
    result.add("".join(perm))

print(len(result))
