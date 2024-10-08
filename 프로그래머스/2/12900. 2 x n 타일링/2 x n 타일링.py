def solution(n):
    answer = 0
    num1 = 1
    num2 = 0
    
    while n > 0 :
        answer = (num1+num2)%1000000007
        num2 = num1
        num1 = answer
        n -= 1
    
    return answer