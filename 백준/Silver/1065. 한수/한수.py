import sys

n = int(sys.stdin.readline())

cnt = 0

for i in range(1, n + 1):
    n = list(str(i))
    # 1, 2 자릿 수는 개수 더해주고 패스
    if len(n) == 1 or len(n) == 2:
        cnt += 1
        continue

    # 한수 아니면 패스
    diff = int(n[0]) - int(n[1])
    for i in range(1, len(n) - 1):
        if int(n[i]) - int(n[i+1]) != diff:
            cnt -= 1
            break
    cnt += 1

print(cnt)
