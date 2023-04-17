import sys

W,N = map(int,sys.stdin.readline().split())

data = []
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    data.append((a,b))

data.sort(lambda x:-x[1])

res = 0
for i in data:
    W -= i[0]
    # print('W:',W)
    if W > 0:
        res += i[0]*i[1]
    else:
        sub = i[0] + W
        res += sub*i[1]
        # print('sub:',sub)
        break

# print('data:',data)
print(res)