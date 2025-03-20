import heapq
import sys

def dijkstra(graph, start, n):
    distance = [float('inf')] * (n + 1)
    distance[k] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distance[current_node]:
            continue
        
        for next_node, d in graph[current_node]:
            new_distance = d + current_distance
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(pq, (new_distance, next_node))
    
    return distance

data = sys.stdin.readlines()

n, e = map(int, data[0].split(" "))
k = int(data[1]) # 시작점
graph = {i : [] for i in range(1, n + 1)}
for i in range(2, e + 2):
    u, v, w = map(int, data[i].split(" "))
    graph[u].append((v, w))
    # graph[v].append((u, w))

distance = dijkstra(graph, k, n)
for i in range(1, n + 1):
    print(distance[i] if distance != float('inf') else "INF")