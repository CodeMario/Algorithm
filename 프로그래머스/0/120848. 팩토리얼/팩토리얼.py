def solution(n):
    answer = 0
    acc = 1
    count = 1
    while acc <= n :
        count += 1
        acc *= count
    answer = count -1
    return answer