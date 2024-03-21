import sys

x, y = map(int, sys.stdin.readline().split())

sum = 0

for i in range(1, x + 1):
    if i == 1:
        continue
    elif i == 3:
        sum += 28
    elif i == 5 or i == 7 or i == 10 or i == 12:
        sum += 30
    else:
        sum += 31

sum += y
x_day = sum % 7

if x_day == 1:
    print("MON")
elif x_day == 2:
    print("TUE")
elif x_day == 3:
    print("WED")
elif x_day == 4:
    print("THU")
elif x_day == 5:
    print("FRI")
elif x_day == 6:
    print("SAT")
else:
    print("SUN")
