def getMinBag(n):
    x, y = 0, -1

    for i in range(n // 3 + 1):
        if (n - i * 3) % 5 == 0:
            x = (n - i * 3) // 5
            y = i
            break

    return x + y

def getMinBagDP(n):
    dp = [-1] * (n + 1)
    if n >= 3:
        dp[3] = 1
    if n >= 5:
        dp[5] = 1
    
    for i in range(6, n + 1):
        if dp[i - 3] != -1 and dp[i - 5] != -1:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1
        elif dp[i - 3] != -1:
            dp[i] = dp[i - 3] + 1
        elif dp[i - 5] != -1:
            dp[i] = dp[i - 5] + 1
    
    return dp[n]

n = int(input())
print(getMinBag(n))
print(getMinBagDP(n))