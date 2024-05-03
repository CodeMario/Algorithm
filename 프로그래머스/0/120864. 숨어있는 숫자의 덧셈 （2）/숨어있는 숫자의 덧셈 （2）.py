def solution(my_string):
    answer = 0
    acc = '0'
    for i in my_string :
        if i >= '0' and i <= '9' :
            acc += i
            continue
        answer += int(acc)
        acc = '0'
    answer += int(acc)
    return answer