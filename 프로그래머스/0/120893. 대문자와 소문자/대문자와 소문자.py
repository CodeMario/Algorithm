def solution(my_string):
    answer = ''
    num = ord('a')
    for i in my_string :
        if ord(i) >= num :
            answer += i.upper()
        else :
            answer += i.lower()
    return answer