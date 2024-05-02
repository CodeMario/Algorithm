def solution(myString):
    answer = ''
    el = ord('l')
    for i in myString :
        if ord(i) < el :
            answer += 'l'
        else :
            answer += i
    return answer