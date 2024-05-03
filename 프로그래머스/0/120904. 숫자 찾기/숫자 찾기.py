def solution(num, k):
    answer = -1
    num = str(num)
    k = str(k)
    if k in num :
        answer = num.index(k) +1
    return answer