def solution(myString, pat):
    answer = ''
    for i in range(len(myString)-1,-1,-1) :
        if myString[i-len(pat)+1:i+1] == pat :
            answer = myString[:i+1]
            break
    return answer