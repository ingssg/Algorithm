import sys

input = sys.stdin.readline


# 스택에 넣어가면서 큰 놈이 나올때마다 가장 앞으로 보내준다. 이때 pop할때마다 k개수 감소, k가 0이 되면 뒤에 그냥 다 넣기
def ans():
    n, k = map(int, input().split())
    nums = list(input().strip())
    stack = []

    for num in nums:        # 모든 입력 값에 대해
        if not stack:       # 스택이 비어있으면 그냥 추가
            stack.append(num)
            continue
        while stack and stack[-1] < num and k > 0:  # 스택에 들어있는 값이 현재 넣어줄 값보다 작을 경우 pop(k번 반복)
            stack.pop()
            k -= 1
        stack.append(num)   # 뺄만큼 다 뺐으니까 그대로 넣어줌

    for _ in range(k):  #  54321 같은 경우 k값에 관계없이 스택에 다 들어가기 때문에 k번만큼 팝
        stack.pop()

    print("".join(stack))


ans()
