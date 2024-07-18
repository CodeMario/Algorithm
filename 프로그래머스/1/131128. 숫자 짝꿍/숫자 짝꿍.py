def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1) :
        numX = X.count(str(i))
        numY = Y.count(str(i))
        answer += min(numX,numY)*str(i)
       
    if answer == '' :
        answer = '-1'
    elif answer == len(answer)*'0' :
        answer = '0'
        
    return answer