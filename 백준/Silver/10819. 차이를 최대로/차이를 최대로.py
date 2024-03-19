import sys
import itertools

n = int(sys.stdin.readline())
datas = list(map(int, sys.stdin.readline().split()))

p_datas = []
result = set()

for i in itertools.permutations(datas):
    p_datas.append(i)
    sum = 0
    for j in range(len(i) - 1):
        sum += abs(i[j] - i[j+1])
    result.add(sum)

print(max(result))
