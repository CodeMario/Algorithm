def solution(arr):
    answer = []
    num = 0
    while len(arr) > 2**num :
        num += 1
    arr += [0]*((2**num)-len(arr))
    answer = arr
    return answer