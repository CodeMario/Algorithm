def solution(n, w, num):
    answer = 0
    n -= 1
    num -= 1
    answer = (n//w) - (num//w)

    n1 = n%w
    n2 = num%w
    
    if (n//w) % 2 != (num//w) % 2 :
        if n1 + n2 + 2> w :
            answer += 1

    else :
        if n1 >= n2 :
            answer += 1

    return answer