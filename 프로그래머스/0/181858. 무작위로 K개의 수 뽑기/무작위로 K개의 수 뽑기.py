def solution(arr, k):
    answer = []
    for i in arr :
        if i in answer :
            continue
        answer.append(i)
        if len(answer) == k :
            break
    for j in range(k-len(answer)) :
        answer.append(-1)
    return answer