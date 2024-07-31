def solution(msg):
    answer = []
    word = [chr(x) for x in range(65, 91)]
    idx = 0
    temp = ''
    while idx < len(msg) :
        temp += msg[idx]
        if temp not in word :
            answer.append(word.index(temp[:-1])+1)
            word.append(temp)
            temp = msg[idx]
        idx += 1
        
    if temp in word :
        answer.append(word.index(temp)+1)
    else :
        answer.append(word.index(temp[:-1])+1)
        answer.append(word.index(temp[-1]+1))
    return answer