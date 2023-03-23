import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if scoville[0] < K:
            if len(scoville) == 1:
                return -1
            min_1 = heapq.heappop(scoville)
            min_2 = heapq.heappop(scoville)
            rep = min_1 + min_2*2
            heapq.heappush(scoville,rep)
            cnt += 1
        else:
            break
    
    return cnt