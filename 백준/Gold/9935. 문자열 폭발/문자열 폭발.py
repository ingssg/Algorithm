import sys

input = sys.stdin.readline


def ans():
    a = list(input().strip())
    b = input().strip()
    stack = []
    result = ''

    for i in a:

        if i not in b:
            stack.append(i)
        else:
            stack.append(i)
            result = ''.join(stack[-len(b):])
            while True:
                if b in result:
                    for _ in range(len(b)):
                        stack.pop()
                    result = ''.join(stack[-len(b):])
                else:
                    break

    if not stack:
        print('FRULA')
    else:
        print(''.join(stack))


ans()
