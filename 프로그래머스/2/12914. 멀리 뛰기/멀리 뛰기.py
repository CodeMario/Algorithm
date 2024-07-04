def solution(n):
    answer = 0
    n1 = 1
    n2 = 2
    if n == 1 :
        answer = n1 
    elif n == 2 :
        answer = n2
    else :
        while n > 2 :
            temp = n1+n2
            n1 = n2
            n2 = temp
            n -= 1
        
        answer = n2%1234567
    return answer