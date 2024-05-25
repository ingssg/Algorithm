import sys

input = sys.stdin.readline


def ans():
    data = list(input().strip())
    stk = []
    cnt = 0
    open_cnt = 0
    for d in data:
        stk.append(d)
        if d == '(':
            open_cnt += 1
        else:
            open_cnt -= 1
            if stk[-2] == '(':
                cnt += open_cnt
            else:
                cnt += 1

    print(cnt)


ans()
