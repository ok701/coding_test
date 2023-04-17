import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

H,W = map(int,input().split())
graph = []
for i in range(H):
    graph.append(list(input().rstrip()))  

dx = [0,1,0,-1]     # 오른,아래,왼,위 
dy = [1,0,-1,0]

# 시작 위치 구하기
breaker = False
for x in range(H):
    for y in range(W):
        cnt = 0
        if graph[x][y] == '#':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<H and 0<=ny<W and graph[nx][ny] == '#':
                    cnt += 1
            if cnt == 1:
                x0,y0 = x,y
                breaker = True
                break
    if breaker == True:
        break

path = []
def dfs(x,y):
    graph[x][y] = '.'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<H and 0<=ny<W and graph[nx][ny] == '#':
            path.append(i)
            dfs(nx,ny)
    return


dfs(x0,y0)              # path 만들기
print(x0+1,y0+1)        # 초기 위치
dir = ['>','v','<','^']
print(dir[path[0]])     # 초기 방향

# 명령어 출력
A_ = False
for i in range(1,len(path)):
    if path[i] == path[i-1]:
        if A_ == True:
            A_ = False
            continue
        A_ = True       # A가 있으니 다음에 A 한번 더 나오면 무시
        print('A',end='')    
    elif path[i] == path[i-1]+1 or path[i] == path[i-1]-3:
        A_ = False
        print('R',end='')
    elif path[i] == path[i-1]-1 or path[i] == path[i-1]+3:
        A_ = False
        print('L',end='')