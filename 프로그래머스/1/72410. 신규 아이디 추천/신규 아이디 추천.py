def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    sign = ['-','_','.']
    for i in new_id :
        #2단계
        if (i>='a' and i<='z')or(i>='0'and i<='9')or(i in sign) :
            #3,4-1 단계
            if (i == '.') and (len(answer)==0 or i == answer[-1]) :
                continue
            answer += i       
    
    n = len(answer)
    
    #4-2단계
    while n != 0 :
        if answer[-1] == '.':
            answer = answer[:-1]
        else :
            break
    
    n = len(answer)
    #6단계
    if n > 15 :
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]
    #5,7단계
    elif n < 3 :
        if n == 0 :
            answer = 'a'*3
        else :
            answer += answer[-1]*(3-n)

    return answer