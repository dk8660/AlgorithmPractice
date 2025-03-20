def LIS(a):
    dp = [1] * len(a)

    for i in range(1, len(a)):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

n = int(input())
a = list(map(int, input().split(" ")))

print(LIS(a))