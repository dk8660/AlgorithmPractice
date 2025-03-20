def getMaxValueBy2D(n, k, w, v):
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(w[i], k + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

    return dp[n - 1][k]

def getMaxValue(n, k, w, v):
    dp = [0] * (k + 1)

    for i in range(n):
        for j in range(k, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    
    return dp[k]

n, k = map(int, input().split(" "))
w, v = [0] * n, [0] * n

for i in range(n):
    w[i], v[i] = map(int, input().split(" "))

print(getMaxValue(n, k, w, v))