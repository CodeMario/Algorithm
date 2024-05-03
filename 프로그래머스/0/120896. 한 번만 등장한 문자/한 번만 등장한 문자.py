def solution(s):
    answer = []
    for i in s :
        if s.count(i) == 1 :
            answer.append(i)
    answer.sort()
    answer = ''.join(answer)
    return answer