def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))
    while len(storey) != 1 :
        n = storey.pop()
        
        if n == 5 :
            answer += 5
            if storey[-1] >= 5 :
                storey[-1] += 1   
        elif n < 5 :
            answer += n
        else :
            answer += 10-n
            storey[-1] += 1
    
    if storey[0] <= 5 :
        answer += storey[0]
    else :
        answer += 11-storey[0]
    return answer