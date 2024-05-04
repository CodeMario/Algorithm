def solution(picture, k):
    answer = []
    for i in range(len(picture)) :
        temp = ''
        for j in picture[i] :
            temp += j*k
        answer += [temp]*k
    return answer