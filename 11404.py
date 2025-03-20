import sys

def floyd_warshall(graph, n):
    distance = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        distance[i][i] = 0
    
    for u in range(1, n + 1):
        for v, w in graph[u]:
            distance[u][v] = min(distance[u][v], w)
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

n = int(input())
m = int(input())
graph = {i : [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    # graph[v].append((u, w))

distance = floyd_warshall(graph, n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(distance[i][j] if distance[i][j] != float('inf') else 0, end=" ")
    print()