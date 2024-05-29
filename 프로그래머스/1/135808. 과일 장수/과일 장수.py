def solution(k, m, score):
    answer = 0
    price = {}
    for i in range(1,k+1) :
        price[i] = score.count(i)
        
    for i in range(k,0,-1) :
        answer += (price[i]//m)*i*m
        if i != 1 :
            price[i-1] += (price[i]%m)
            
    return answer