import sys

input = sys.stdin.readline

def ans():
    s = input().strip()
    n = int(input())
    lines = [input().strip() for _ in range(n)]
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1
    for i in range(len(s)):
        if dp[i] == 1:
            for l in lines:
                for j in range(len(l)):
                    if i+j >= len(s) or s[i+j] != l[j]:
                        break
                    if j == len(l)-1:
                        dp[i+j+1] = 1   # l과 같은 부분이면 그 다음 인덱스에 1값 추가 후 그 값부터 다시 탐색

    print(dp[-1])   # 모든 부분이 같으면 마지막 인덱스가 1이된다.


ans()
