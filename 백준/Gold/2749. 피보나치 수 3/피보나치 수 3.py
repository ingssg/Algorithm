import sys

input = sys.stdin.readline


# 피사노 주기: 피보나치 수를 k로 나눈 나머지는 항상 주기를 갖게 된다.
# 나머지가 10**k 일때
# 주기 : 10**(k-1) * 15
def ans():
    n = int(input())
    mod = 1000000
    mod_p = (mod // 10) * 15
    dp = [0] * (mod_p + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, mod_p):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
    print(dp[n % mod_p])


ans()
