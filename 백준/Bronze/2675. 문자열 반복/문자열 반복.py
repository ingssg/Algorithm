import sys

t = int(sys.stdin.readline())
cases = [sys.stdin.readline().strip() for i in range(t)]

for case in cases:
    result = ""
    case = case.split(" ")
    for i in range(len(case[1])):
        result += case[1][i] * int(case[0])
    print(result)
