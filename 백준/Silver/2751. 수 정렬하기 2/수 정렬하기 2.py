list=[]
num = int(input())

for _ in range(num):
  list.append(int(input()))

list.sort()

for i in range(len(list)):
  print(list[i])