import sys

c = int(sys.stdin.readline())
datas = [list(map(int, sys.stdin.readline().split())) for i in range(c)]

for data in datas:
    overScoreCnt = 0
    average = (sum(data) - data[0]) / data[0]
    for score in data:
        if(score == data[0]):
            continue
        if(score > average):
            overScoreCnt += 1
    print("{:.3f}%".format(overScoreCnt/data[0]*100))
