def solution(n, arr1, arr2):
    answer = ['']*n
    for i in range(n) :
        for j in range(n-1,-1,-1) :
            if arr1[i]//(2**j)+arr2[i]//(2**j) > 0:
                answer[i] += '#'
            else :
                answer[i] += ' '
            arr1[i] %= (2**j)
            arr2[i] %= (2**j)
            
    return answer