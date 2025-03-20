def getChunk(trees, m):
    left, right = 0, trees[len(trees) - 1]

    while left <= right:
        mid = (left + right) // 2
        chunk = sum((tree - mid) for tree in trees if tree > mid)

        if chunk >= m:
            left = mid + 1
        else:
            right = mid - 1
            
    return right

n, m = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
trees.sort()
print(getChunk(trees, m))