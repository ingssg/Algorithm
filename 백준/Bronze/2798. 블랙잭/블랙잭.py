import sys

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m:
                break
            if cards[i] + cards[j] + cards[k] > max and cards[i] + cards[j] + cards[k] <= m:
                max = cards[i] + cards[j] + cards[k]
print(max)
