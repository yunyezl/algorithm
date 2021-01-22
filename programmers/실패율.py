def solution(N, stages):
    answer = []    
    dem = len(stages)
    
    for i in range(1, N+1):
        num = stages.count(i)
        if dem > 0:
            answer.append((i , num / dem))
        else:
            answer.append((i, 0))
        dem -= num
    
    answer.sort(key = lambda x:x[1], reverse=True)
        
    result = []
    for i in answer:
        result.append(i[0])
    
    return result
