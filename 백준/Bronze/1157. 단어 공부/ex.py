text = input().upper()
maxCount = 0
maxAlpha = "?"
for i in range(ord("A"),ord("Z")+1):
    C = text.count(chr(i))
    if C > maxCount:
        maxCount = C
        maxAlpha = chr(i)
    elif C == maxCount:
        maxAlpha = "?"
        
print(maxAlpha)
