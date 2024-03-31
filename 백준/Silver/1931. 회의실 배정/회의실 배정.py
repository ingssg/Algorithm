import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    meeting = [list(map(int, input().split())) for _ in range(n)]
    meeting.sort(key=lambda x: (x[1], x[0]))
    que = []
    que.append(meeting[0])
    while que:
        for i in range(1, n):
            if que[-1][1] > meeting[i][0]:
                continue
            que.append(meeting[i])
        break
    print(len(que))


ans()
