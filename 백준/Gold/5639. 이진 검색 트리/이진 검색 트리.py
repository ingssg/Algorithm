import sys
sys.setrecursionlimit(10**8)

datas = []
while True:
    try:
        data = int(sys.stdin.readline())
        datas.append(data)
    except:
        break


def ans(nodes):
    if not nodes:
        return []
    left_nodes = []
    right_nodes = []
    root = nodes[0]
    for i in range(1, len(nodes)):
        if nodes[i] < root:
            left_nodes.append(nodes[i])
        else:
            right_nodes.append(nodes[i])

    left_result = ans(left_nodes)
    right_result = ans(right_nodes)

    return left_result + right_result + [root]

for data in ans(datas):
    print(data)
