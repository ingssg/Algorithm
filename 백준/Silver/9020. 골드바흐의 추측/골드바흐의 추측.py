import math
import sys

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
input = []
for _ in range(n):
    input.append(int(sys.stdin.readline()))

for num in input:
    results = []
    incresedNum = num // 2
    decresedNum = num // 2

    for _ in range(num//2 - 1):
        if (isPrime(incresedNum) and isPrime(decresedNum)):
            print(decresedNum, incresedNum)
            break
        incresedNum += 1
        decresedNum -= 1
