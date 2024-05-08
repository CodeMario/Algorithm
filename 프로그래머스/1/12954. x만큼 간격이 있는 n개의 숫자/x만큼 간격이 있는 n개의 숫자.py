def solution(x, n):
    if x != 0 :
        addition = 1
        if x < 0 :
            addition -= 2
        answer = list(range(x,x*n+addition,x))
    else :
        answer = [0]*n
    
    return answer