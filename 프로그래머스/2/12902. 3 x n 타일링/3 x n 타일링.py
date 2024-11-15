def solution(n):
    answer = 0
    if n % 2 == 0 :
        n1 = 1
        n2 = 1
        for i in range(2,n+1,2) :
            temp = n2
            n2 = (n2*4)-n1
            if n2 < 0 :
                n2 += 1000000007
            n2 %= 1000000007
            n1 = temp
        answer = n2
    return answer