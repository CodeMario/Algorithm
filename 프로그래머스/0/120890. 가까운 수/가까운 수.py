def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    i = array.index(n)
    
    if i == 0 :
        answer = array[1]
    elif i == len(array)-1 :
        answer = array[-2]
    elif n-array[i-1] <= array[i+1]-n :
        answer = array[i-1]
    else :
        answer = array[i+1]
    
    return answer