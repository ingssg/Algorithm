import sys

n = int(sys.stdin.readline())
n_data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_data = list(map(int, sys.stdin.readline().split()))

n_data.sort()

def is_in_arr(arr, key):
    left = 0
    right = len(arr)-1

    while True:
        center = (left + right) // 2
        if key == arr[center]:
            return 1
        elif key < arr[center]:
            right = center - 1
        elif key > arr[center]:
            left = center + 1
        if right < left:
            return 0


for data in m_data:
    print(is_in_arr(n_data, data))
    