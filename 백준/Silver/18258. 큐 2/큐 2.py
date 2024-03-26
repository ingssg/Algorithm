import sys
from collections import deque

n = int(sys.stdin.readline())


def push(queue, k):
    queue.append(k)


def pop(queue):
    if not queue:
        sys.stdout.write(str(-1) + '\n')
        return
    print(queue.popleft())


def size(queue):
    return len(queue)


def empty(queue):
    return 0 if queue else 1


def front(queue):
    if not queue:
        return -1
    return queue[0]


def back(queue):
    if not queue:
        return -1
    return queue[-1]


def solve(n):
    test = deque()
    for i in range(n):
        data = sys.stdin.readline().strip().split()
        if data[0] == 'push':
            push(test, int(data[1]))
        elif data[0] == 'front':
            sys.stdout.write(str(front(test)) + '\n')
        elif data[0] == 'back':
            sys.stdout.write(str(back(test)) + '\n')
        elif data[0] == 'size':
            sys.stdout.write(str(size(test)) + '\n')
        elif data[0] == 'empty':
            sys.stdout.write(str(empty(test)) + '\n')
        elif data[0] == 'pop':
            pop(test)

solve(n)
