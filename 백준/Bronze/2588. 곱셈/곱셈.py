import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
sum = 0
cnt = 1
while(y):
    print(x*(y%10))
    sum += x * (y % 10) * cnt
    y //= 10
    cnt *= 10
print(sum)
