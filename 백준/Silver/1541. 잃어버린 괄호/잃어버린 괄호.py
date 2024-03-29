import sys

input = sys.stdin.readline


# 마이너스 나오면 다시 마이너스 만날때까지 괄호 묶기
def ans():
    data = input().strip()
    split_data = data.split('-') # -로 문자열 자르기
    _sum = 0
    for idx, d in enumerate(split_data):
        split_d = d.split('+')
        if idx == 0:
            _sum += sum(int(num) for num in split_d)
        else:
            _sum -= sum(int(num) for num in split_d)
    print(_sum)


ans()
