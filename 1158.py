n, k = input().split(" ")
n = int(n)
k = int(k)

circle = list()
for i in range(1, n + 1):
    circle.append(i)

result = list()

index = 0
for i in range(n):
    for i in range(k - 1):
        index += 1
        if index == len(circle):
            index = 0
    result.append(circle.pop(index))
    if index == len(circle):
        index = 0

for i in range(n):
    if(i == 0):
        print("<", end="")
    if(i < n - 1):
        print(result[i], end=", ")
    if(i == n - 1):
        print(result[i], end="")
        print(">")