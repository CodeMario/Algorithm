def solution(n):
    answer = ''
    while(n >= 1):
        temp = n % 3
        n = n // 3
        
        if temp == 0 :
            temp = 4
            n-=1
        answer += str(temp)
            
    return answer[::-1]