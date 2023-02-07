N = int(input())

error = False

for i in range((N//3)+1):  
  times5 = (N - 3*i) 
  if times5%5 == 0:
    error = False
    break
  error = True

j = times5//5

if not error:
  print(i+j)
else:
  print(-1)
