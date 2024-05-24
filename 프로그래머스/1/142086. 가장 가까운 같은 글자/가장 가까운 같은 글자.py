def solution(s):
    answer = []
    location = {}
    for i in range(len(s)) :
        temp = s[i]
        if temp in location :
            answer.append(i-location[temp])
        else :
            answer.append(-1)
        location[temp] = i
    return answer