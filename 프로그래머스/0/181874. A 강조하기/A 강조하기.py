def solution(myString):
    answer = ''
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == ' ' or myString[i] == 'A' :
            continue
        elif myString[i] == 'a' :
            myString[i] = 'A'
        else :
            myString[i] = myString[i].lower()
    answer = ''.join(myString)
    return answer