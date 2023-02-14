# N:종류 K:합
N, K = map(int,input().split()) 

list=[]
for _ in range(N):
  list.append(int(input()))
#list.sort(reverse=True)
#print(list)

res = 0
while(K!=0):
  max_coin_num = K//max(list)
  
  K = K - max_coin_num*max(list)
  list.remove(max(list))
  res = res+max_coin_num
  #print(res)

print(res)
