def solution(fees, records):
    answer = []
    acc = {}
    
    for i in records[::-1] :
        time,number,io = i.split()
        time = (int(time[:2])*60)+(int(time[3:5]))
        if io == 'IN' :
            if number in acc :
                acc[number] -= time
            else :
                acc[number] = 1439-time
        else :
            if number in acc :
                acc[number] += time
            else :
                acc[number] = time
    answer = list(acc.keys())
    answer.sort()

    for i in range(len(answer)) :
        temp = acc[answer[i]]
        if temp > fees[0] :
            temp -= fees[0]
            if temp%fees[2] != 0 :
                temp += fees[2]
            temp = (temp//fees[2])*fees[3]+fees[1]
            
            
        else :
            temp = fees[1]
        
        answer[i] = temp
    return answer