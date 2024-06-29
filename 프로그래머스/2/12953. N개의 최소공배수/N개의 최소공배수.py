def solution(arr):
    answer = 0
    while len(arr) > 1 :
        tempArr = arr[:2]
        while True :
            temp = tempArr[0] % tempArr[1]
            if temp == 0 :
                del tempArr[0]
                break
            tempArr[0] = tempArr[1]
            tempArr[1] = temp
        arr[1] = arr[0]*arr[1]//tempArr[0]
        del arr[0]
    answer = arr[0]
    return answer