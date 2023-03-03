from collections import deque

test_case = int(input())  # 3

for _ in range(test_case):
  
  N, M = map(int,input().split())  # N:4 문서 갯수, M:2 알고 싶은 문서
  
  queue = list(map(int,input().split()))  # 1 2 3 4
  max_ = max(queue)
  queue_ = deque((i,v) for i,v in enumerate(queue))
  
  # print('queue_: ',queue_)
  cnt = 0
  
  while(True):
  
    
    if queue_[0][1] == max_:
      # print('queue_[0][0]: ',queue_[0][0], 'M: ',M)
      if queue_[0][0] == M:
        break
      pop = queue_.popleft()
      queue.remove(max_)
      max_ = max(queue)
      cnt += 1
    
  
    
    else:
      pop = queue_.popleft()
      queue_.append(pop)
      # print(queue_)
    
  print(cnt+1)