import sys

input = sys.stdin.readline


def ans():
    while True:
        stack = []
        datas = list(map(int, input().split()))
        if datas[0] == 0:
            return
        n = datas[0]
        datas.append(0)
        _max = 0

        for i in range(1, n+2):
            start = i
            while stack and stack[-1][1] > datas[i]:
                start, height = stack.pop()
                _max = max(_max, (i - start)*height)
            stack.append([start, datas[i]])

        print(_max)


ans()
