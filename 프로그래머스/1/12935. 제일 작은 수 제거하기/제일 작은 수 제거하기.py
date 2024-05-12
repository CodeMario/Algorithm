def solution(arr):
    answer = arr
    answer.remove(min(answer))
    if answer == [] :
        answer = [-1]
    return answer