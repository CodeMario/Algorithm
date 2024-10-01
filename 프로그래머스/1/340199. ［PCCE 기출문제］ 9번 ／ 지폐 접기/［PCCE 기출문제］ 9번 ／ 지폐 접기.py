def solution(wallet, bill):
    answer = 0
    w1 = max(wallet)
    w2 = min(wallet)
    b1 = max(bill)
    b2 = min(bill)
    temp = 0
    
    while w1 < b1 or w2 < b2 :
        b1 = b1 // 2
        if b1 < b2 :
            temp = b1
            b1 = b2
            b2 = temp
        answer += 1
    return answer