def solution(s):
    answer = ''
    flag = True
    for i in s :
        if flag :
            if i == ' ' :
                answer += i
                continue
            flag = False
            answer += i.upper()
            continue
        
        if i == ' ' :
            flag = True
            
        answer += i.lower()
    return answer