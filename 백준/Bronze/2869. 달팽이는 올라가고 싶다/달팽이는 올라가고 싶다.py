import sys

a, b, v = map(int, sys.stdin.readline().split())

climb_day = 0

if((v-a)%(a-b) == 0):
    climb_day = (v-a)//(a-b) + 1
else:
    climb_day = (v - a) // (a - b) + 2
    
print(climb_day)
