import sys

def findLatestInScope(db, L, R):
    selectedData = db[L : R + 1]
    

n = int(input())
db = []

for _ in range(n):
    id, timestamp = map(int, sys.stdin.readline().split())
    db.append(id, timestamp)

db.sort()