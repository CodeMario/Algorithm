def solution(n, words):
    answer = [1,1]
    last = words[0][-1]
    flag = True
    used = [words[0]]
    
    for i in range(1,len(words)) :
        answer[0] += 1
        if answer[0] > n :
            answer[0] = 1
            answer[1] += 1
            
        if(words[i] in used)or(last!=words[i][0]):
            flag = False
            break
        else :
            last = words[i][-1]
            used.append(words[i])
    
    if flag :
        answer = [0,0]
        
    return answer