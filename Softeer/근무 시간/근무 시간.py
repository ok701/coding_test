import sys

res = 0
for _ in range(5):
    a,b = sys.stdin.readline().split()

    start_H = int(a[0]+a[1])
    start_M = int(a[-2]+a[-1])
    start_time = start_H*60 + start_M

    end_H = int(b[0]+b[1])
    end_M = int(b[-2]+b[-1])
    end_time = end_H*60 + end_M

    res += end_time - start_time

print(res)