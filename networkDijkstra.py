import sys
import heapq

def getMaxMinBW(s, e, bw, n):
    minBw = [float('inf')] * (n + 1)
    heap = list()
    for nextNode, w in bw[s]:
        heapq.heappush(heap, (-1 * w, nextNode, s))
    
    while heap:
        w, nextNode, currentNode = heapq.heappop(heap)
        if minBw[nextNode] != float('inf'): continue
        w *= -1
        minBw[nextNode] = min(minBw[currentNode], w)
        if nextNode == e: break
        for v, w in bw[nextNode]:
            heapq.heappush(heap, (-1 * w, v, nextNode))
    
    return minBw[e]

n, m = map(int, sys.stdin.readline().split())
bw = {i : [] for i in range(1, n + 1)}
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    bw[u].append((v, w))
    bw[v].append((u, w))
s, e = map(int, sys.stdin.readline().split())

print(f"최대 최소 대역폭 = {getMaxMinBW(s, e, bw, n)}")