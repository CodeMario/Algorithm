def solution(N, stages):
    answer = []
    clear = [0] * (N+1)
    clearRate = []
    for i in stages :
        clear[i-1] += 1
        
    for i in range(N) :
        temp = sum(clear[i:])
        if temp == 0 :
            clearRate.append([i+1,0])
        else :
            clearRate.append([i+1,clear[i]/temp])
    
    clearRate.sort(key = lambda x : (-x[1],x[0]))
    
    for i in range(N) :
        answer.append(clearRate[i][0])
    return answer