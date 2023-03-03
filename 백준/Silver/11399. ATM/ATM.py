# N = 5
# time = [3,1,4,3,2]


N = int(input())
time = list(map(int,input().split()))

time.sort()
n = N
total = 0

for i in range(N):
  # print('total: ',total,"n: ",n)
  total += time[i]*n
  n += -1
 

print(total)