x = int(input())
a = 0
while x >= 0:
    if x % 5 == 0:
        a += (x//5)
        print(a)
        break
    x = x - 3
    a = a + 1
else:
    print(-1)
