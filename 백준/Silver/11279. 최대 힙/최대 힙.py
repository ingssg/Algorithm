import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
datas = [int(sys.stdin.readline()) for _ in range(n)]


def push_print(q, x):
    if x == 0:
        if q.empty():
            print(0)
            return
        _x = q.get()
        print(-_x)
    else:
        q.put(-x)

def ans(datas):
    queue = PriorityQueue()
    for data in datas:
        push_print(queue, data)

ans(datas)
