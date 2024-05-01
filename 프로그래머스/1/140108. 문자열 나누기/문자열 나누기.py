def solution(s):
    answer = 0
    accSame = 0
    accDiff = 0
    firstWord = ""

    for i in s :
        #딕셔너리에 이미 있는지 확인
        if firstWord == "" :
            accSame += 1
            firstWord = i
            answer += 1
            continue
        
        elif i == firstWord :
            accSame += 1
        else :
            accDiff += 1

        #첫글자가 아닌데 첫글자랑 나온 횟수가 같아질 때
        if accSame == accDiff :
            accSame = 0
            accDiff = 0
            firstWord = ""

    return answer