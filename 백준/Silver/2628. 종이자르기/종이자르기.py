import sys
def calc_length(data):
    max = 0
    for i in range(len(data) - 1):
        if data[i + 1] - data[i] > max:
            max = data[i + 1] - data[i]
    return max

w, h = map(int, sys.stdin.readline().split())
cutNum = int(sys.stdin.readline())
datas = [sys.stdin.readline().strip() for i in range(cutNum)]

# datas[0] == 0 > 가로로 자르는 점선, 1 > 세로로 자르는 점선
# datas[1] > 몇 번째 줄 자를지

# 다 나열한 후 그 차이가 가장 적은 값으로 곱하기

width = [0, w]
height = [0, h]
for data in datas:
    data = list(map(int, data.split()))
    # 가로줄 자르기
    if data[0] == 0:
        height.append(data[1])
    # 세로줄 자르기
    else:
        width.append(data[1])
width.sort()
height.sort()
print(calc_length(width) * calc_length(height))
