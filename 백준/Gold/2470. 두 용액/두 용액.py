import sys

n = int(sys.stdin.readline())
datas = list(map(int, sys.stdin.readline().split()))
datas.sort()


def yong(arr):

    l = len(arr)
    left = 0
    right = l - 1
    _min = abs(arr[left] + arr[right])
    result_left = arr[left]
    result_right = arr[right]
    while left < right:
        if arr[left] + arr[right] == 0:
            return [arr[left], arr[right]]
        elif arr[left] + arr[right] < 0:
            if abs(arr[left] + arr[right]) < _min:
                _min = abs(arr[left] + arr[right])
                result_left = arr[left]
                result_right = arr[right]
            left += 1
        else:
            if abs(arr[left] + arr[right]) < _min:
                _min = abs(arr[left] + arr[right])
                result_left = arr[left]
                result_right = arr[right]
            right -= 1
    return [result_left, result_right]


ans = yong(datas)
print(ans[0], ans[1])
