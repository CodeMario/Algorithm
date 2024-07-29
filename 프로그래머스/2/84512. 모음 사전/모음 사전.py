def solution(word):
    answer = 0
    trans = {'A':0,'E':1,'I':2,'O':3,'U':4}
    #앞자리의 문자를 바꾸기 위해서는 전 자리가 해당 문자로 바뀌는데 필요한 변화 횟수를 가능한 모든 경우를 거쳐야함 => *5+1
    num = [781,156,31,6,1]
    for i in range(len(word)) :
        answer += num[i]*trans[word[i]]+1
    return answer