import sys


def merge_sort(a):
    def _merge_sort(a, left, right):
        if left < right:
            mid = (left + right) // 2
            _merge_sort(a, left, mid)
            _merge_sort(a, mid + 1, right)

            p = j = 0
            i = k = left    # p: buff에 쌓인 개수 / j: buff 0부터 비교 / i: left 부터 비교 / k: a 좌측부터 비교

            while i <= mid:
                buff[p] = a[i]
                p += 1
                i += 1
            while j < p and i <= right:
                if a[i] >= buff[j]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n-1)
    del buff


num = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(num)]

merge_sort(x)

for i in x:
    print(i)
