import sys


def sum_arr(arr):
    _sum = 0
    for inner in arr:
        _sum += sum(inner)
    return _sum


def mul_arr(arr):
    mul = 1
    for inner in arr:
        for num in inner:
            mul *= num
    return mul


def saekjonge(arr, num):
    global zero_cnt
    global one_cnt
    if sum_arr(arr) == 0 or mul_arr(arr) == 1: # 0종이나 1종이면
        if sum_arr(arr) == 0: # 0종이
            zero_cnt += 1
        if mul_arr(arr) == 1: # 1종이
            one_cnt += 1
    else:
        if num != 1:
            temp = []
            temp2 = []
            temp3 = []
            temp4 = []
            for i in range(num):
                if i < num//2:
                    temp.append(arr[i][:num//2])
                    temp2.append(arr[i][num//2:])
                else:
                    temp3.append(arr[i][:num//2])
                    temp4.append(arr[i][num//2:])
            saekjonge(temp, num // 2)
            saekjonge(temp2, num // 2)
            saekjonge(temp3, num // 2)
            saekjonge(temp4, num // 2)

# 요소 곱이 1이면 1 종이, 요소합 0이면 0종이
#  스탑하고 0인지 1인지 체크 후 거기 1or0 cnt += 1
#
# 아니면 잘라야지
# [n//2][n//2] 크기로 자르고 재귀


n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
zero_cnt = 0
one_cnt = 0
saekjonge(data, n)
print(zero_cnt, one_cnt)
