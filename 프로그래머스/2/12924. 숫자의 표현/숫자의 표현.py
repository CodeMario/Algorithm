def solution(n):
    answer = 0
    acc = []
    for i in range(1,n+1) :
        acc.append(i)
        while sum(acc) > n :
            del acc[0]
            
        if sum(acc) == n :
            answer += 1
    return answer