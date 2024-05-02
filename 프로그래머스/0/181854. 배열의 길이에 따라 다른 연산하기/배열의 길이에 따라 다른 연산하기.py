def solution(arr, n):
    startIndex = 0
    if len(arr)%2 == 0 :
        startIndex += 1
    for i in range(startIndex,len(arr),2) :
        arr[i] += n
    return arr