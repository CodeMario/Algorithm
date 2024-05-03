def solution(myString):
    myString = myString.split('x')
    while "" in myString :
        myString.remove("")
    myString.sort()
    answer = myString
    return answer