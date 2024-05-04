def solution(numer1, denom1, numer2, denom2):
    answer = []
    bunja = (numer1*denom2) + (numer2*denom1)
    bunmo = denom1*denom2
    num = 2
    while num <= bunja :
        if bunja%num==0 and bunmo%num==0 :
            bunja/=num
            bunmo/=num
        else :
            num += 1
    answer = [bunja,bunmo]
    return answer