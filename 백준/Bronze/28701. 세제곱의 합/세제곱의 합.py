import sys

n = int(sys.stdin.readline())

a = n*(n+1)//2
sum = 0
for i in range(1, n+1):
    sum += i*i*i

print(a)
print(a * a)
print(sum)
