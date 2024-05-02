def solution(my_string):
    answer = 0
    for i in my_string :
        if ord(i) >= ord('0') and ord(i) <= ord('9') :
            answer += int(i)
    return answer