import sys

datas = [int(sys.stdin.readline()) for i in range(3)]

result = str(datas[0] * datas[1] * datas[2])

for i in range(10):
    cnt = 0
    for num in result:
        if(str(i) == num):
            cnt += 1
    print(cnt)
