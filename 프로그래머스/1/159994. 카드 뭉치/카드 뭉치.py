def solution(cards1, cards2, goal):
    answer = 'Yes'
    index1 = 0
    index2 = 0
    for i in goal :
        if i == cards1[index1] :
            index1 += 1
            if index1 == len(cards1) :
                index1 = index2
                cards1 = cards2
        elif i == cards2[index2] :
            index2 += 1
            if index2 == len(cards2) :
                index2 = index1
                cards2 = cards1
        else :
            answer = 'No'
            break
            
    return answer