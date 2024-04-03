import sys

input = sys.stdin.readline

def ans():
    n = int(input())
    tasks = [list(map(int, input().split())) for _ in range(n)]
    tasks.sort(key=lambda x: (-x[1], x[0]))

    time = tasks[0][1]
    for t in tasks:
        during, dead = t
        if time < dead:
            time -= during
        else:
            time = dead - during
    if time < 0:
        print(-1)
    else:
        print(time)


ans()
