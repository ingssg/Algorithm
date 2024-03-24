import sys

input = sys.stdin.readline

# 모든 타워를 스택에 넣어주는데, 이 때 스택에서 자기보다 작은 탑 값들은 다 팝 하고 큰거의 타워 번호 출력 
# 스택이 비었으면 0 출력

def ans():
    n = int(input())
    towers = list(map(int, input().split()))
    stack = []
    for i, tower in enumerate(towers, start=1):
        while stack:
            if tower > stack[-1][0]:    # 스택[탑]의 높이가 현재 타워보다 작으면
                stack.pop()
            else:
                print(stack[-1][1], end=' ') # 현재 높이보다 크면 출력
                break
        else:
            print(0, end=' ')
        stack.append([tower, i])    # 타워높이, 타워 번호


ans()
