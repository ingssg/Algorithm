import sys
from collections import deque

input = sys.stdin.readline


# 벽이나 자기 자신의 몸과 부딪히면 끝
# 사과 먹으면 꼬리는 가만히 머리만 사과위치로
# 이동시 꼬리 한칸 이동


# 해당 좌표 큐에 집어 넣음(appendleft), 셋에 집어넣음
# 이동 시 pop하고 그 값 셋에서 제거

# 벽의 경우
# 이동 방향으로 + 1 or -1 했을 때 하나의 좌표가 0이거나 n+1이면 죽은 것

# 자기 몸에 부딪히는 경우
# 만약 appendleft 하고 셋에 집어 넣었는데 셋의 크기가 안 변하면 죽은 것

def ans():
    n = int(input())  # 보드 크기
    k = int(input())  # 사과 개수
    board = [[False] * n for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        board[a - 1][b - 1] = True
    l = int(input())  # 뱀 방향 변환 횟수
    c = []
    for _ in range(l):
        a, b = map(str, input().strip().split())
        c.append([a, b])
    c = deque(sorted(c, key=lambda x: (int(x[0]), x[1])))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 우, 하, 좌, 상
    time = 0
    snake = deque()
    visited = set()
    x = y = 1
    snake.appendleft((1, 1))
    visited.add((1, 1))

    dir = ['-10', 'trash']
    if len(c) > 0:
        dir = c.popleft()
    d = 0
    while True:
        # print(x, y)
        if time == int(dir[0]):
            if dir[1] == 'L':
                d -= 1
            if dir[1] == 'D':
                d += 1
            if len(c) > 0:
                dir = c.popleft()
        time += 1
        x += directions[d%4][0]
        y += directions[d%4][1]
        if x > n or y > n or x == 0 or y == 0:  # 벽에 닿은 경우
            break
        snake.appendleft((x, y))
        tmp_visited = len(visited)
        visited.add((x, y))
        if tmp_visited == len(visited):  # 자기 자신에 닿은 경우
            break
        if board[y - 1][x - 1]:  # 사과 먹는 위치면
            board[y - 1][x - 1] = False
        else:
            tail = snake.pop()  # 꼬리 위치 옮기기
            visited.remove(tail)

    print(time)


ans()
