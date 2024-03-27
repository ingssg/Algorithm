import sys
import heapq

input = sys.stdin.readline


def ans():
    n = int(input())
    left = []  # 최대힙
    right = []  # 최소힙

    for i in range(n):
        num = int(input())
        if i % 2 == 0:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)
        if left and right:
            a = right[0]
            b = left[0]
            if a < -b:
                heapq.heappop(right)
                heapq.heappop(left)
                heapq.heappush(right, -b)
                heapq.heappush(left, -a)

        print(-left[0])


ans()
