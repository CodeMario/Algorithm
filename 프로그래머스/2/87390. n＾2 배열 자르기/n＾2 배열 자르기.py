def solution(n, left, right):
    answer = []
    lr = left//n
    lc = left%n
    rr = right//n
    rc = right%n
    
    for i in range(lr,rr+1) :
        temp = []
        answer += [i+1]*(i+1)
        for j in range(i+1,n) :
            temp += [j+1]
        answer += temp
    
    answer = answer[lc:(rr-lr)*n+rc+1]
    return answer