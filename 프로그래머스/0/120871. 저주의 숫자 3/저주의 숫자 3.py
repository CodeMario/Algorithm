def solution(n):
    answer = 1
    while n != 0 :
        if '3' in str(answer) or answer%3==0:
            answer += 1
        else :
            answer += 1
            n -= 1
    answer -= 1
    return answer