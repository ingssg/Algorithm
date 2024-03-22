import sys

n = int(sys.stdin.readline())
inputs = [list(sys.stdin.readline().strip().split(' ')) for _ in range(n)]


class Node:
    def __init__(self, val=None, left='.', right='.'):
        self.val = val
        self.left = left
        self.right = right


# 전위 순회
def root_first(node):
    if node.val == '.':
        return
    print(node.val, end='')
    if node.left != '.':
        root_first(nodes[node.left])
    if node.right != '.':
        root_first(nodes[node.right])


# 중위 순회
def root_second(node):
    if node.val == '.':
        return
    if node.left != '.':
        root_second(nodes[node.left])
    print(node.val, end='')
    if node.right != '.':
        root_second(nodes[node.right])


# 후위 순회
def root_last(node):
    if node.val == '.':
        return
    if node.left != '.':
        root_last(nodes[node.left])
    if node.right != '.':
        root_last(nodes[node.right])
    print(node.val, end='')


nodes = {}

for node in inputs:
    nodes[node[0]] = Node(node[0], node[1], node[2])
root_first(nodes['A'])
print()
root_second(nodes['A'])
print()
root_last(nodes['A'])
