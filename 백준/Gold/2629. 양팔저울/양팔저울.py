import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    chu = list(map(int, input().split()))
    o_num = int(input())
    oo = list(map(int, input().split()))
    dp = [0]
    for c in chu:
        tmp = []
        for i in dp:
            tmp.append(i+c)
            tmp.append(abs(i-c))
        dp = list(set((dp + tmp)))

    for o in oo:
        print('Y' if o in dp else 'N', end=" ")


ans()
