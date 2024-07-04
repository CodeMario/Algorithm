def solution(want, number, discount):
    answer = 0
    n = sum(number)
    dic = dict(zip(want,number))
    for i in range(len(discount)-n+1) :
        temp = dict(zip(want,[0]*len(want)))
        for j in range(i,i+n) :
            if discount[j] in temp :
                temp[discount[j]] += 1
        if dic == temp :
            answer += 1
    
    return answer