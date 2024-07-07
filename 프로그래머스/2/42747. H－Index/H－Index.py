def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    n = len(citations)
    for i in range(n) :
        if citations[i] > answer :
            answer = i+1
        else :
            break
    return answer