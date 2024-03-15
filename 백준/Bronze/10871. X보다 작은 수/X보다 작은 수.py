import sys

n, x = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

result = ""

for i, num in enumerate(data):
    if(i+1 > n):
        break
    if(num < x):
        result += str(num) + " "
print(result.strip())
