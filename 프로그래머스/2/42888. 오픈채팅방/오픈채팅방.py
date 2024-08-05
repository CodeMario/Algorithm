def solution(record):
    answer = []
    name = {}
    cmd = []
    for i in record :
        temp = i.split()
        if temp[0] == 'Change' :
            name[temp[1]] = temp[2]
        else :
            if temp[0] == 'Enter' :
                name[temp[1]] = temp[2]
            cmd.append([temp[1],temp[0]])
            
    for i in cmd :
        result = name[i[0]]+'님이 '
        if i[1] == 'Enter' :
            result += '들어왔습니다.'
        else :
            result += '나갔습니다.'
        answer.append(result)
    return answer