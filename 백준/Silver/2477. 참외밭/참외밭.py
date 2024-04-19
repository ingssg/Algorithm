import sys

input = sys.stdin.readline


# 가장 긴거 두개 뽑고, 가장 긴거 앞뒤에 있는거를 반대쪽 꺼에서 빼기
# 가장 긴거 곱한거 - 가장 긴거 앞뒤에 있는거 반대쪽에서 뺀거 끼리 곱한거
def ans():
    k = int(input())
    batt = []
    max_w = 0
    max_h = 0
    w_idx = -1
    h_idx = -1
    for i in range(6):
        dir, length = map(int, input().split())
        batt.append([dir, length])
        if dir == 1 or dir == 2:
            if max_w < length:
                max_w = length
                w_idx = i
        else:
            if max_h < length:
                max_h = length
                h_idx = i
    rest_h = max_h - min(batt[(w_idx - 1) % 6][1], batt[(w_idx + 1) % 6][1])
    rest_w = max_w - min(batt[(h_idx - 1) % 6][1], batt[(h_idx + 1) % 6][1])

    print((max_w * max_h - rest_w * rest_h) * k)


ans()
