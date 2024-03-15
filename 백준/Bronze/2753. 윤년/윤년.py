import sys

year = int(sys.stdin.readline())

# 0 : False, 1: True
isLeap = 0

if(year % 4 == 0):
    if(year % 100 != 0 or year % 400 == 0):
        isLeap = 1

print(isLeap)
