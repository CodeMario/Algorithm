def solution(dartResult):
    answer = [0]*4
    temp = ''
    option = {'S':1,'D':2,'T':3,'*':2,'#':-1}
    index = 1
    for i in dartResult :
        if i in option :
            if i == '*' :
                answer[index-1] *= option[i]
                answer[index-2] *= option[i]
            elif i == '#' :
                answer[index-1] *= option[i]
            else :
                answer[index] += int(temp)**option[i]
                temp = ''
                index += 1
        else :
            temp += i
    
    return sum(answer)