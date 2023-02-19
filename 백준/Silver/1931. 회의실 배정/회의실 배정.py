from sys import stdin

tot_num = int(input())

courses = []
for _ in range(tot_num):
  courses.append(list(map(int, stdin.readline().split())))

courses.sort(key = lambda x: x[0])
courses.sort(key = lambda x: x[1])

loc_min = courses[0][1]
cnt = 1

for i in range(1,tot_num):
  if courses[i][0] >= loc_min:
    cnt += 1
    loc_min = courses[i][1]
  

print(cnt)