last_king,last_rock,N = input().split()

rows =     ['A','B','C','D','E','F','G','H']
rows_num = [0,1,2,3,4,5,6,7]
cols =     ['1','2','3','4','5','6','7','8']
cols_num = [7,6,5,4,3,2,1,0]

# 체스 위치를 배열의 형태로 바꿈
king = []
rock = []
for i in range(len(rows)):
  if last_king[0] == rows[i]:
    king.append(rows_num[i])
  if last_rock[0] == rows[i]:
    rock.append(rows_num[i])
for i in range(len(cols)):
  if last_king[1] == cols[i]:
    king.append(cols_num[i])
  if last_rock[1] == cols[i]:
    rock.append(cols_num[i])
# print(king,rock)

lists=[]
for _ in range(int(N)):
  lists.append(input())
  
dx =         [ 1,    1,   1,   0,   0,  -1,  -1,  -1]
dy =         [-1,    0,   1,  -1,   1,  -1,   0,   1]
move_types = ['RT','R','RB', 'T', 'B','LT', 'L','LB']


last_x = king[0]
last_y = king[1]
last_rock_x = rock[0]
last_rock_y = rock[1]
rock_x = rock[0]
rock_y = rock[1]
cnt = 0


for list in lists:
  i = move_types.index(list)
  
  x = last_x + dx[i]
  y = last_y + dy[i]

  # 돌 위치 파악
  if x == last_rock_x and y == last_rock_y:
      rock_x = last_rock_x + dx[i]
      rock_y = last_rock_y + dy[i]

  if x < 0 or x>7 or y<0 or y>7 or rock_x < 0 or rock_x>7 or rock_y<0 or rock_y>7:
      x = last_x
      y = last_y
      rock_x = last_rock_x
      rock_y = last_rock_y
      cnt = cnt+1

  else:
      last_x = x
      last_y = y
      last_rock_x = rock_x
      last_rock_y = rock_y
      cnt = cnt+1

  if cnt == int(N):
    print(rows[rows_num.index(x)]+cols[cols_num.index(y)])
    print(rows[rows_num.index(rock_x)]+cols[cols_num.index(rock_y)])
  
