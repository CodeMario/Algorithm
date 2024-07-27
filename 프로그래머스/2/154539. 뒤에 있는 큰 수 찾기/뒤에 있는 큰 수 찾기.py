def solution(numbers):
    answer = [-1]
    lp, rp = len(numbers)-2,len(numbers)-1
    
    while lp >= 0 :
        if numbers[lp] < numbers[rp] :
            answer.append(numbers[rp])
            rp = lp
            lp -= 1
            
        elif rp == len(numbers)-1 :
            answer.append(-1)
            rp = lp
            lp -= 1
        
        else :
            del numbers[rp]
    
    return answer[::-1]