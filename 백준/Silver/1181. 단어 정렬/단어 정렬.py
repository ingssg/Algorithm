import sys


def sortt(arr):
    len_set = set()
    same_len_list = []

    for i in range(len(arr)):
        if not len(arr[i]) in len_set:
            len_set.add(len(arr[i]))

    len_list = list(len_set)
    len_list.sort()

    for data in len_list:
        tmp_list = []
        for i in range(len(arr)):
            if len(arr[i]) == data:
                tmp_list.append(arr[i])
        tmp_list.sort()
        same_len_list.append(tmp_list)

    return same_len_list


n = int(sys.stdin.readline())
lists = []

for _ in range(n):
    a = sys.stdin.readline().strip()
    if a in lists:
        continue
    else:
        lists.append(a)

answer = sortt(lists)

for out_list in answer:
    for i in out_list:
        print(i)
