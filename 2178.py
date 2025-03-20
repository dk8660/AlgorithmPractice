from collections import deque

def detectBFS():
    count = 0
    queue = deque([(0, 0, 0)])
    check = [[False] * m for i in range(n)]
    while(True):
        x, y, count = queue.popleft()
        if not check[x][y] and matrix[x][y]:
            check[x][y] = True
            count += 1

            if x == n - 1 and y == m - 1:   
                break

            if x < n - 1 and matrix[x + 1][y]:
                queue.append((x + 1, y, count))
            if y < m - 1 and matrix[x][y + 1]:
                queue.append((x, y + 1, count))
            if x > 0 and matrix[x - 1][y]:
                queue.append((x - 1, y, count))
            if y > 0 and matrix[x][y - 1]:
                queue.append((x, y - 1, count))

    return count

n, m = map(int, input().split(" "))
matrix = list()
for i in range(n):
    l = list(map(int, input()))
    matrix.append(l)

print(detectBFS())