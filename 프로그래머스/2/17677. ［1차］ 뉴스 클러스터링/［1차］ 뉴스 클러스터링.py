def Counting(s) :
    answer = 0
    temp = ''
    cnt = {}
    for i in s :
        if i >= 'A' and i <= 'Z' :
            temp += i 
        else :
            temp = ''
        
        if len(temp) == 2 :
            if temp in cnt :
                cnt[temp] += 1
            else :
                cnt[temp] = 1
            temp = i
    return cnt

def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    cntA = Counting(str1)
    cntB = Counting(str2)
    if len(cntA) +len(cntB) == 0 :
        answer = 1
    else :
        temp = [0,0]
        key = set(list(cntA.keys())+list(cntB.keys()))
        for i in key :
            if i not in cntA :
                temp[1] += cntB[i]
            elif i not in cntB :
                temp[1] += cntA[i]
            else :
                temp[0] += min(cntA[i],cntB[i])
                temp[1] += max(cntA[i],cntB[i])
        answer = temp[0] / temp[1]
    
    answer = int(answer*65536)
    return answer