import sys

n = int(sys.stdin.readline())
sticks = [int(sys.stdin.readline()) for _ in range(n)]


def calc_sticks(sticks):
    cnt = 1  # 시작부터 하나 보임
    top = sticks[-1]  # 가장 뒤에 값
    for i in range(n - 1, -1, -1):  # 뒤에서부터 조회
        if sticks[i] > top:  # 더 큰 막대기 있으면
            top = sticks[i]  # 가장 큰 값 갱신
            cnt += 1  # 개수 갱신
    print(cnt)


calc_sticks(sticks)
