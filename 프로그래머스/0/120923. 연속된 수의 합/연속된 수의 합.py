def solution(num, total):
    answer = list(range(0,num))
    while sum(answer) != total :
        if sum(answer) > total :
            answer.insert(0,answer[0]-1)
            del answer[-1]
        else :
            answer.append(answer[-1]+1)
            del answer[0]
    return answer