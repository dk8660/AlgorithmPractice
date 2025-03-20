import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)

def setParentDFS(tree, parent, node, depth):
    for child in tree[node]:
        if parent[child] == 0:
            parent[child] = node
            depth[child] = depth[node] + 1
            setParentDFS(tree, parent, child, depth)

def setParentBFS(tree, parent, root, depth):
    queue = deque()
    queue.append(root)
    
    while queue:
        p = queue.popleft()
        for child in tree[p]:
            if parent[child] == 0:
                parent[child] = p
                depth[child] = depth[p] + 1
                queue.append(child)

def getParent(parent, node):
    return parent[node]

def LCA(parent, a, b):
    while depth[a] > depth[b]:
        a = getParent(parent, a)
    while depth[b] > depth[a]:
        b = getParent(parent, b)
    
    while a != b:
        a = getParent(parent, a)
        b = getParent(parent, b)
    
    return a

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = list(map(int, input().split(" ")))
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n + 1)
parent[1] = -1
depth = [0] * (n + 1)
# setParentDFS(tree, parent, 1, depth)
setParentBFS(tree, parent, 1, depth)

m = int(input())
nodes = list()
for i in range(m):
    nodes.append(map(int, input().split(" ")))

for i in range(m):
    a, b = nodes[i]
    print(LCA(parent, a, b))