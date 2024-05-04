def solution(strArr):
    answer = 0
    length = {}
    for i in strArr :
        n = len(i)
        if n in length :
            length[n] += 1
        else :
            length[n] = 1
        if length[n] > answer :
                answer = length[n]
    return answer