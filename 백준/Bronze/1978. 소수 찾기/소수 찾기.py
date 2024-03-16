import sys

n = int(sys.stdin.readline())
datas = list(map(int, sys.stdin.readline().split()))

result = 0

for data in datas:
    if(data == 1):
        continue
    cnt = 0
    for i in range(2, data):
        if(data % i == 0):
            cnt+=1
            break
    if cnt==0:
        result += 1

print(result)
