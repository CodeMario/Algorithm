def solution(arr):
    answer = [[]]
    row = len(arr[0])
    col = len(arr)
    
    answer = arr
    if row == col :
        return answer
    elif row > col :
        for i in range(row-col) :
            answer.append([0]*row)
    else :
        for i in range(col) :
            answer[i] += [0]*(col-row)
    return answer