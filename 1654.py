def findBestLongest(lines, n):
    left, right = 1, lines[len(lines) - 1]
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for line in lines:
            count += line // mid
        
        if count >= n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

k, n = map(int, input().split(" "))
lines = list()
for _ in range(k):
    lines.append(int(input()))
lines.sort()
print(findBestLongest(lines, n))