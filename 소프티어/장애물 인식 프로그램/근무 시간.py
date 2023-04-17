import sys

N = int(input())
data = []
for _ in  range(N):
    line = sys.stdin.readline().rstrip()
    data.append([int(s) for s in line])

def dfs(x,y):
    global num
    if x<0 or x>N-1 or y<0 or y>N-1:
        return False
    if data[x][y] == 1:
        data[x][y] = 0
        num += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True     # 방문할때가 더이상 없음
    return False


num = 0
cnt = 0
Num = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            num = 0
            dfs(i,j)
            cnt += 1
            Num.append(num)

Num.sort()        
print(cnt)
for i in range(cnt):
    print(Num[i]) 