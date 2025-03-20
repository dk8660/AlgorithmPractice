import sys

def bellman_ford(graph, n, start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    
    for _ in range(n - 1):
        for u in range(1, n + 1):
            for v, w in graph[u]:
                if distance[u] != float('inf') and distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
    
    for u in range(1, n + 1):
            for v, w in graph[u]:
                if distance[u] != float('inf') and distance[v] > distance[u] + w:
                    print("음수 사이클 존재")
                    return None
    
    return distance

n = int(input())
m = int(input())
graph = {i : [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

start = int(input())
distance = bellman_ford(graph, n, start)

if distance:
    print(" ".join(str(d if d != float('inf') else -1) for d in distance[1:]))