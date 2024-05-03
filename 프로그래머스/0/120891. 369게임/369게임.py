def solution(order):
    answer = 0
    clap = ['3','6','9']
    order = str(order)
    for i in order :
        if i in clap :
            answer +=1
    return answer