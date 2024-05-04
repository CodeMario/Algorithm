def solution(array):
    answer = 0
    while len(array) > 1 :
        temp = list(set(array))
        for i in temp :
            array.remove(i)
        
    if len(array) == 1:
        answer = array[0]
    else :
        answer = -1
    return answer