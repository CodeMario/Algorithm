def solution(strArr):
    answer = []
    switch = True
    for i in strArr :
        if switch :
            answer.append(i.lower())
            switch = False
        else :
            answer.append(i.upper())
            switch = True
    return answer