def solution(order):
    answer = 0
    sub = [0]
    temp = 0
    for i in order :
        if i > sub[-1] :
            sub += list(range(temp+1,i))
            temp = i
            answer += 1
        elif i == sub[-1] :
            sub.pop()
            answer += 1
        else :
            break
    
    return answer