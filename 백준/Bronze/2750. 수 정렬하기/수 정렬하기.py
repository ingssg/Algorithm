import sys


def binary_insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        pl = 0
        pr = i - 1
        key = array[i]

        while True:
            pc = (pl + pr) // 2
            if array[pc] == key:
                break
            if array[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            array[j] = array[j-1]
        array[pd] = key


num = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(num)]

binary_insertion_sort(x)

for num in x:
    print(num)
