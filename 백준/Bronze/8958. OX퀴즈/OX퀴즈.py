import sys

n = int(sys.stdin.readline())
datas = [sys.stdin.readline().strip() for i in range(n)]

for data in (datas):
    sum = 0
    inc_num = 1
    for result in (data):
        if(result == "O"):
            sum += inc_num
            inc_num += 1
        else:
            inc_num = 1
    print(sum)
