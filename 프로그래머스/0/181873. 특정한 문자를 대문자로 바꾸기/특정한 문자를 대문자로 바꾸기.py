def solution(my_string, alp):
    answer = ''
    for i in my_string :
        if i != alp :
            answer += i
        else :
            answer += i.upper()
    return answer