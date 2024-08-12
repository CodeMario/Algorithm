from collections import Counter

def solution(weights):
    answer = 0
    types = Counter(weights)
    for i in types :
        answer += types[i]*(types[i]-1)//2
        answer += types[i]*types[i*2/3]
        answer += types[i]*types[i*2/4]
        answer += types[i]*types[i*3/4]
    return answer