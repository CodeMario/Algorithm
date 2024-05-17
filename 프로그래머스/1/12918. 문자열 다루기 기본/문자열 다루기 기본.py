def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6 :
        for i in s :
            if i < '0' or i > '9' :
                answer = False
                break
    else :
        answer = False
    return answer