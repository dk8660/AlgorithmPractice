from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.edge = list()
    
def setEdge(x, y):
    graph[x].edge.append(y)
    graph[y].edge.append(x)
    graph[x].edge.sort()
    graph[y].edge.sort()

def DFS(now):
    result.append(graph[now].data)
    check[now] = True
    for e in graph[now].edge:
        if not check[e]:
            DFS(e)

def BFS(now):
    check[now] = True
    result.append(graph[now].data)
    for e in graph[now].edge:
        queue.append(e)
    while(queue):
        now = queue.popleft()
        if not check[now]:
            check[now] = True
            result.append(graph[now].data)
            for e in graph[now].edge:
                queue.append(e)

n, k, start = map(int, input().split(" "))

graph = list()
for i in range(1, n + 1):
    graph.append(Node(i))

for i in range(k):
    x, y = map(int, input().split(" "))
    setEdge(x - 1, y - 1)

check = list()
now = start - 1
for i in range(n):
    check.append(False)

result = list()
DFS(now)

for r in result:
    print(r, end=" ")
print()

queue = deque()
result = list()
for i in range(n):
    check[i] = False

BFS(now)
for r in result:
    print(r, end=" ")