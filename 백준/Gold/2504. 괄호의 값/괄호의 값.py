import sys

data = sys.stdin.readline().strip()


def ans(data):
    if len(data) % 2 != 0:
        return 0

    stack = []
    result = 0
    remaining = 1

    for index, i in enumerate(data, start=0):
        if i == '(' or i == '[':
            stack.append(i)
            if i == '(':
                remaining *= 2
            else:
                remaining *= 3
        elif i == ')':
            if stack:
                if stack[-1] != '(':
                    return 0
                else:
                    if data[index -1] == '(':
                        result += remaining
                    stack.pop()
                    remaining //= 2
            else:
                return 0
        else:  # i == ']'
            if stack:
                if stack[-1] != '[':
                    return 0
                else:
                    if data[index -1] == '[':
                        result += remaining
                    stack.pop()
                    remaining //= 3
            else:
                return 0
    if stack:
        return 0

    return result


print(ans(data))
