import sys

k = int(sys.stdin.readline())
datas = [int(sys.stdin.readline()) for _ in range(k)]


def pop(arr):
    arr = arr[:-1]
    return arr


stack = []

for data in datas:
    if data == 0:
        stack = pop(stack)
    else:
        stack.append(data)

print(sum(stack))
