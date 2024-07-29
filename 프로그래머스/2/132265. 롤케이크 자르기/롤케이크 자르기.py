def solution(topping):
    answer = 0
    cntA = set()
    cntB = {}
    for i in topping :
        cntB[str(i)] = cntB.get(str(i), 0)
        cntB[str(i)] += 1
    
    for i in topping :
        cntA.add(i)
        cntB[str(i)] -= 1
        if cntB[str(i)] == 0 :
            del cntB[str(i)]
        
        if len(cntA) == len(cntB) :
            answer += 1
        
    return answer