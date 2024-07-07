def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes :
        if i[1] in dic :
            dic[i[1]] += 1
        else :
            dic[i[1]] = 1
    key = list(dic.keys())
    
    for i in key :
        answer *= (dic[i]+1)
        
    return answer-1