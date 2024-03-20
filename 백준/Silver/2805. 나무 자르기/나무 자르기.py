import sys

n, m = map(int, sys.stdin.readline().split())
datas = list(map(int, sys.stdin.readline().split()))


def cut_tree(arr, key):
    result = 0
    left = 0
    right = max(datas)

    while True:
        center = (left + right) // 2
        temp_sum = 0
        for a in arr:
            if a > center:
                temp_sum += a-center
        if temp_sum == key:
            result = center
            break
        elif temp_sum > key:
            result = center
            left = center + 1
        elif temp_sum < key:
            right = center - 1
        if left > right:
            break
    return result


print(cut_tree(datas, m))
