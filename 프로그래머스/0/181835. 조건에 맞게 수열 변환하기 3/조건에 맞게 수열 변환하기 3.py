def solution(arr, k):
    flag = 0
    if k % 2 == 0 :
        flag = 1
    
    for i in range(len(arr)) :
        if flag == 0 :
            arr[i] *= k
        else :
            arr[i] += k
        
    return arr