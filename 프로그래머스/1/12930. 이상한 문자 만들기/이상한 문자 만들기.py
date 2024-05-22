def solution(s):
    answer = ''
    flag = 0
    for i in s :
        if i == ' ' :
            answer += i
            flag = 1
        elif flag == 1 :
            answer += i.lower()
        else :
            answer += i.upper()
        flag = abs(flag-1)
            
    return answer