def solution(i, j, k):
    answer = 0
    k = str(k)
    for n in range(i,j+1) :
        n = list(str(n))
        if k in n :
            for m in n :
                if m == k :
                    answer += 1
    return answer