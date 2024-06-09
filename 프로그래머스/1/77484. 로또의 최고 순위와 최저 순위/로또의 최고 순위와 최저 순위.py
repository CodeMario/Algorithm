def solution(lottos, win_nums):
    answer = []
    correct = 0
    unknown = 0
    
    for i in lottos :
        if i == 0 :
            unknown += 1
        elif i in win_nums :
            correct += 1
            
    temp = correct+unknown
    if temp < 2 :
        answer.append(6)
    else :
        answer.append(7-(temp))
    if correct == 0 :
        correct = 1
    answer.append(7-(correct))
    return answer