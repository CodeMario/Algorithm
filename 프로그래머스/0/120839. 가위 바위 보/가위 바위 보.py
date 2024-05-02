def solution(rsp):
    answer = ''
    hand = {'2':'0','0':'5','5':'2'}
    for i in rsp :
        answer += hand[i]
    return answer