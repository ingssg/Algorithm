import sys

input = sys.stdin.readline


def ans():
    m, n = map(int, input().split())
    alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    datas = []

    for i in range(m, n + 1):
        str_ = ""
        while i > 0:
            str_ = alp[i % 10] + str_
            i //= 10
            if i > 0:
                str_ = " " + str_
        datas.append(str_)
    datas.sort()

    txts = []
    for d in datas:
        txt = ""
        nums = d.split()
        for n in nums:
            txt = txt + str(alp.index(n))
        txts.append(txt)

    for idx, t in enumerate(txts):
        if idx and idx%10 == 0:
            print()
        print(t, end =" ")


ans()
