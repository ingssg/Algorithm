import sys

n = int(sys.stdin.readline())
datas = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]


def is_ok(case):
    if len(case) % 2 != 0:  # 2의 배수가 아닐 때
        print("NO")
        return

    def pop(arr):
        return arr[:-1]

    stack = []
    for data in case:
        if data == '(':
            stack.append(data)
        else:
            if not stack:       # 다음 값이 ) 인데  스택이 비어 있는 경우 no
                print("NO")
                return
            stack = pop(stack)  # 다음 값이 ) 이면 팝
    if stack:       # 다 조사 했을 때 안에 내용이 있으면 no
        print("NO")
    else:
        print("YES")


for i in datas:
    is_ok(i)
