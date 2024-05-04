def solution(numlist, n):
    for i in range(len(numlist)) :
        numlist[i] = [numlist[i],abs(n-numlist[i])]
    answer = sorted(numlist,key=lambda x:(x[1], -x[0]))
    for i in range(len(answer)) :
        answer[i] = answer[i][0]
     
    return answer