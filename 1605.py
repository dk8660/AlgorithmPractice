def rolling_hashing(s, w):
    base, mod = 31, 2 ** 61 - 1
    h = set()
    val = 0
    power = 1

    for i in range(w):
        val = (val * base + ord(s[i])) % mod
        if i < w - 1:
            power = (power * base) % mod
    
    h.add(val)

    for i in range(w, len(s)):
        val = (val - ord(s[i - w]) * power) % mod
        val = (val * base + ord(s[i])) % mod
    
        if val in h:
            return True
        h.add(val)
    
    return False

def getMaxSubstringLength(s, l):
    left, right= 1, l
    while left <= right:
        w = (left + right) // 2
        if rolling_hashing(s, w):
            left = w + 1
        else:
            right = w - 1
    
    return right

l = int(input())
s = input()

print(getMaxSubstringLength(s, l))