def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for i in babbling :
        temp = ''
        before = ''
        flag = True
        for j in i :
            temp += j
            if temp in word :
                if before == temp :
                    flag = False
                    break
                before = temp
                temp = ''
        if temp != '' :
            flag = False
            
        if flag :
            answer += 1
                
    return answer