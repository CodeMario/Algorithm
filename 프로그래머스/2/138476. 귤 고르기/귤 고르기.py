def solution(k, tangerine):
    answer = 0
    size = {}
    for i in tangerine :
        if i in size :
            size[i] += 1
        else :
            size[i] = 1
            
    size = list(size.values())
    size.sort(reverse=True)
    for i in size :
        k -= i
        answer += 1
        if k <= 0 :
            break
    return answer