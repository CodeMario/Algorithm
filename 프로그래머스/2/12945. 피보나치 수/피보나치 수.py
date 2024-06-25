def solution(n):
    answer = 0
    n1 = 0
    n2 = 1
    for i in range(2,n+1) :
        temp = n1+n2
        n1 = n2
        n2 = temp
        
    answer = n2%1234567
    return answer