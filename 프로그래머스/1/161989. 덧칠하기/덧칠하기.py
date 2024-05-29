def solution(n, m, section):
    answer = 0
    location = 0
    for i in section :
        if location >= i :
            continue
        else :
            location = i+m-1
            answer += 1
    return answer