import sys

n = int(sys.stdin.readline())
datas = [sys.stdin.readline().strip() for _ in range(n)]


def push(arr: list, x):
    arr.append(x)


def pop(arr: list):
    if not arr:
        print(-1)
        return arr
    last = arr[-1]
    arr = arr[:-1]
    print(last)
    return arr


def size(arr):
    print(len(arr))


def empty(arr):
    if arr:
        print(0)
    else:
        print(1)


def top(arr):
    if not arr:
        print(-1)
    else:
        print(arr[-1])


stack = []

for inst in datas:
    inst = inst.split(' ')
    if inst[0] == 'push':
        push(stack, int(inst[1]))
    elif inst[0] == 'top':
        top(stack)
    elif inst[0] == 'size':
        size(stack)
    elif inst[0] == 'empty':
        empty(stack)
    else:
        stack = pop(stack)
