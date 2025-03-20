from collections import deque

n = int(input())
words = list()
for i in range(n):
    words.append(input())

count = 0
for word in words:
    isGroupWord = True
    stack = deque()
    for i in range(len(word)):
        if i == 0:
            stack.append(word[i])
            continue
        
        if word[i] != word[i - 1]:
            if word[i] in stack:
                isGroupWord = False
                break
            
            stack.append(word[i])
    
    if isGroupWord:
        count += 1

print(count)