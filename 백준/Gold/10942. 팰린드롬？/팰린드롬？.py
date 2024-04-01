import sys

input = sys.stdin.readline


def ans():
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    q = [list(map(int, input().split())) for _ in range(m)]
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for start in range(n - i):
            end = start + i
            if start == end:    #  시작과 끝이 같은 경우 == 길이가 1인 경우 > 펠린드롬
                dp[start][end] = 1
            elif nums[start] == nums[end]:  # 문자열 양 끝이 같은경우에...
                if start + 1 == end:    # 길이가 2인 경우 펠린드롬
                    dp[start][end] = 1
                elif dp[start + 1][end - 1] == 1:   # 안의 문자열이 펠린드롬인 경우 펠린드롬
                    dp[start][end] = 1

    for que in q:
        print(dp[que[0] - 1][que[1] - 1])


ans()
