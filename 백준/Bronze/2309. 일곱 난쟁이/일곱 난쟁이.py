import sys

datas = []
jjap_nanj = []

for _ in range(9):
    datas.append(int(sys.stdin.readline()))
datas.sort()
sum = sum(datas)

for i in range(9):
    for j in range(i+1, 9):
        if sum - datas[i] - datas[j] == 100:
            jjap_nanj.append(datas[i])
            jjap_nanj.append(datas[j])
            i = 9
            break

for data in datas:
    if data != jjap_nanj[0] and data != jjap_nanj[1]:
        print(data)
        